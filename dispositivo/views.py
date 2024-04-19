from .models import Dispositivo
from rest_framework.decorators import action
from .serializers import DispositivoSerializer, DispositivoWriteSerializer
from inventario.utils import generate_search_field
from inventario.common.base import BaseViewSet
from rest_framework.permissions import IsAuthenticated
from .filter import DispositivoFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from aula.models import Aula
from aula_dispositivo.models import AulaDispositivo
from aula_dispositivo.serializers import AulaDispositivoWriteSerializer
from rest_framework.parsers import FileUploadParser
from django.http import HttpResponse
import io
from django.db import transaction


class DispositivoViewSet(BaseViewSet):
    permission_classes = [IsAuthenticated]
    default_serializer_class = DispositivoSerializer
    filterset_class = DispositivoFilter
    default_serializer_class = DispositivoSerializer
    serializer_classes = {
        "list": DispositivoSerializer,
        "retrieve": DispositivoSerializer,
        "create": DispositivoWriteSerializer,
        "update": DispositivoWriteSerializer,
        "partial_update": DispositivoWriteSerializer,
    }
    response_classes = {
        "create": DispositivoSerializer,
        "update": DispositivoSerializer,
        "partial_update": DispositivoSerializer,
    }
    swagger_tags = ["api/dispositivo"]

    def get_queryset(self):
        return Dispositivo.objects.all()

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user, updated_by=self.request.user, search=generate_search_field(serializer.validated_data["codigo_dispositivo"]))
    
    def perform_update(self, serializer):
        if "codigo_dispositivo" in serializer.validated_data:
            serializer.validated_data["search"] = generate_search_field(serializer.validated_data["codigo_dispositivo"])
        return serializer.save(updated_by=self.request.user)
    


    @action(detail=False, methods=["POST"])
    def upload_dispositivos_excel(self, serializer):
        parser_classes = (FileUploadParser,)
        file = self.request.FILES.get('file')
        if not file:
            return Response({'error': 'No se proporcionó ningún archivo'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            df = pd.read_excel(file)
        except Exception as e:
            return Response({'error': f'Error al leer el archivo Excel: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        
        required_columns = ['Codigo', 'Sucursal', 'Codigo_aula']
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            return Response({'error': f'Faltan las siguientes columnas requeridas: {", ".join(missing_columns)}'}, status=status.HTTP_400_BAD_REQUEST)

        dispositivos_created = []
        processed_codigo_dispositivos = set()
        processed_codigo_aulas = set()
        
        try:
            with transaction.atomic():
                for index, row in df.iterrows():
                    codigo_dispositivo = str(row['Codigo']).strip()
                    codigo_aula = str(row['Codigo_aula']).strip()

                    if codigo_dispositivo in processed_codigo_dispositivos:
                        dispositivos_created.append({'Codigo': codigo_dispositivo, 'status': 'Error', 'message': 'El dispositivo ya está presente en el archivo', 'row_index': index})
                        continue

                    if Dispositivo.objects.filter(codigo_dispositivo=codigo_dispositivo, deleted=False).exists():
                        dispositivos_created.append({'Codigo': codigo_dispositivo, 'status': 'Error', 'message': 'El dispositivo ya existe', 'row_index': index})
                        continue

                    data = {
                        'codigo_dispositivo': codigo_dispositivo,
                    }
                    serializer = DispositivoWriteSerializer(data=data)
                    if serializer.is_valid():
                        if codigo_aula:
                            try:
                                aula = Aula.objects.get(codigo_aula=codigo_aula, deleted=False)
                                if codigo_aula in processed_codigo_aulas:
                                    dispositivos_created.append({'Codigo': codigo_dispositivo, 'status': 'Error', 'message': 'El vehiculo ya se reportó en el archivo', 'row_index': index})
                                    continue
                                processed_codigo_aulas.add(codigo_aula)
                            except Aula.DoesNotExist:
                                dispositivos_created.append({'Codigo': codigo_dispositivo, 'status': 'Error', 'message': 'El vehiculo no existe', 'row_index': index})
                                continue

                            if AulaDispositivo.objects.filter(aula=aula, history=False, deleted=False).exists():
                                dispositivos_created.append({'Codigo': codigo_dispositivo, 'status': 'Error', 'message': 'Ya existe un dispositivo vinculado a este vehiculo.', 'row_index': index})
                                continue

                        serializer.save(created_by=self.request.user, updated_by=self.request.user, search=generate_search_field(codigo_dispositivo))
                        dispositivos_created.append({'codigo_dispositivo': codigo_dispositivo, 'status': 'Success', 'message': 'Dispositivo creado'})
                        dispositivo = Dispositivo.objects.filter( codigo_dispositivo=codigo_dispositivo, deleted=False).first()
                        if codigo_aula:
                            aula_dispositivo_data = {
                                'dispositivo': dispositivo.pk,
                                'aula': aula.pk,
                            }
                            serializerAulaDispositivo = AulaDispositivoWriteSerializer(data=aula_dispositivo_data)
                            if serializerAulaDispositivo.is_valid():
                                serializerAulaDispositivo.save(created_by=self.request.user, updated_by=self.request.user)
                        processed_codigo_dispositivos.add(codigo_dispositivo)
                    else:
                        dispositivos_created.append({'codigo_dispositivo': codigo_dispositivo, 'status': 'Error', 'message': serializer.errors, 'row_index': index})
        except Exception as e:
            return Response({'error': f'Error al procesar el archivo Excel: {str(e)}', 'dispositivos_created': dispositivos_created}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'dispositivos_created': dispositivos_created}, status=status.HTTP_200_OK)
    
    def upload_dispositivos_excel(self, serializer):
        parser_classes = (FileUploadParser,)
        file = self.request.FILES.get('file')
        if not file:
            return Response({'error': 'No se proporcionó ningún archivo'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            df = pd.read_excel(file)
        except Exception as e:
            return Response({'error': f'Error al leer el archivo Excel: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        
        required_columns = ['Codigo', 'Sucursal', 'Codigo_aula']
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            return Response({'error': f'Faltan las siguientes columnas requeridas: {", ".join(missing_columns)}'}, status=status.HTTP_400_BAD_REQUEST)

        dispositivos_created = []
        processed_codigo_dispositivos = set()
        processed_codigo_aulas = set()
        for index, row in df.iterrows():
            codigo_dispositivo = str(row['Codigo']).strip()
            codigo_aula = str(row['Codigo_aula']).strip()

            if codigo_dispositivo in processed_codigo_dispositivos:
                dispositivos_created.append({'Codigo': codigo_dispositivo, 'status': 'Error', 'message': 'El dispositivo ya está presente en el archivo', 'row_index': index})
                continue

            if Dispositivo.objects.filter(codigo_dispositivo=codigo_dispositivo, deleted=False).exists():
                dispositivos_created.append({'Codigo': codigo_dispositivo, 'status': 'Error', 'message': 'El dispositivo ya existe', 'row_index': index})
                continue

            if Dispositivo.objects.filter( codigo_dispositivo=codigo_dispositivo, deleted=False).exists():                
                dispositivos_created.append({'Codigo': codigo_dispositivo, 'status': 'Error', 'message': 'Dispositivo ya esta registrado en esta sucursal', 'row_index': index})
                continue

            data = {
                'codigo_dispositivo': codigo_dispositivo,
            }
            serializer = DispositivoWriteSerializer(data=data)
            if serializer.is_valid():
                if codigo_aula:
                    try:
                        aula = Aula.objects.get(codigo_aula=codigo_aula, deleted=False)
                        if codigo_aula in processed_codigo_aulas:
                            dispositivos_created.append({'Codigo': codigo_dispositivo, 'status': 'Error', 'message': 'El vehiculo ya se reportó en el archivo', 'row_index': index})
                            continue
                        processed_codigo_aulas.add(codigo_aula)
                    except Aula.DoesNotExist:
                        dispositivos_created.append({'Codigo': codigo_dispositivo, 'status': 'Error', 'message': 'El vehiculo no existe', 'row_index': index})
                        continue

                    if AulaDispositivo.objects.filter(aula=aula, history=False, deleted=False).exists():
                        dispositivos_created.append({'Codigo': codigo_dispositivo, 'status': 'Error', 'message': 'Ya existe un dispositivo vinculado a este vehiculo.', 'row_index': index})
                        continue

                serializer.save(created_by=self.request.user, updated_by=self.request.user, search=generate_search_field(codigo_dispositivo))
                dispositivos_created.append({'codigo_dispositivo': codigo_dispositivo, 'status': 'Success', 'message': 'Dispositivo creado'})
                dispositivo = Dispositivo.objects.filter( codigo_dispositivo=codigo_dispositivo, deleted=False).first()
                if codigo_aula:
                    aula_dispositivo_data = {
                        'dispositivo': dispositivo.pk,
                        'aula': aula.pk,
                    }
                    serializerAulaDispositivo = AulaDispositivoWriteSerializer(data=aula_dispositivo_data)
                    if serializerAulaDispositivo.is_valid():
                        serializerAulaDispositivo.save(created_by=self.request.user, updated_by=self.request.user)
                processed_codigo_dispositivos.add(codigo_dispositivo)
            else:
                dispositivos_created.append({'codigo_dispositivo': codigo_dispositivo, 'status': 'Error', 'message': serializer.errors, 'row_index': index})
        return Response({'dispositivos_created': dispositivos_created}, status=status.HTTP_200_OK)

    
    @action(detail=False, methods=["GET"])
    def download_example_excel(self, serializer):
        data = {
            'Codigo': ['Es el codigo serial del dispositivo', 'DEF456', 'GHI789'],
            'Sucursal': ['Es el nombre de la sucursal donde se dar de alta el dispositivo', 'Sucursal B', 'Sucursal C'],
            'Codigo_aula': ['Es el numero economico del vehiculo donde se instalo el dispositvo', 1002, 1003]
        }
        df = pd.DataFrame(data)
        excel_buffer = io.BytesIO()
        df.to_excel(excel_buffer, index=False)
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=Ejemplo_de_dispositivos.xlsx'
        excel_buffer.seek(0)
        response.write(excel_buffer.read())

        return response
        
    @action(detail=False, methods=["GET"])
    def download_format_excel(self, serializer):
        columns = ['Codigo', 'Sucursal', 'Codigo_aula']
        df = pd.DataFrame(columns=columns)
        excel_buffer = io.BytesIO()
        df.to_excel(excel_buffer, index=False)
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=Formato_de_carga_dispositivos.xlsx'
        excel_buffer.seek(0)
        response.write(excel_buffer.read())

        return response

