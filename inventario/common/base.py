from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import models
from django.contrib.auth import get_user_model


class BaseModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class DeleteModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=True)


class BaseModel(models.Model):
    class Meta:
        abstract = True

    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        get_user_model(),
        default=None,
        related_name='%(class)s_created',
        on_delete=models.DO_NOTHING,
    )
    updated_by = models.ForeignKey(
        get_user_model(),
        default=None,
        related_name='%(class)s_updated',
        on_delete=models.DO_NOTHING,
    )

    objects = BaseModelManager()
    deleted_objects = DeleteModelManager()
    all_objects = models.Manager()

    def delete(self):
        self.deleted = True
        self.save()

    def hard_delete(self):
        super().delete()


class CustomFilterBackend(DjangoFilterBackend):
    def get_filterset_class(self, view, queryset=None):
        # ignore model type checking
        return getattr(view, "filterset_class", None)


class BaseViewSet(viewsets.ModelViewSet):
    serializer_classes = {}
    filter_backends = [CustomFilterBackend]

    def get_serializer(self, *args, **kwargs):
        params = self.request.query_params
        serializer_class = self.get_serializer_class()
        kwargs.setdefault("context", self.get_serializer_context())
        return serializer_class(*args, **kwargs)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        retrieve_serializer = self.serializer_classes.get(
            "retrieve", self.default_serializer_class
        )(instance)
        headers = self.get_success_headers(retrieve_serializer.data)
        return Response(
            retrieve_serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        return serializer.save()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        updated_instance = self.perform_update(serializer)
        retrieve_serializer = self.serializer_classes.get(
            "retrieve", self.default_serializer_class
        )(updated_instance)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(retrieve_serializer.data)

    def perform_update(self, serializer):
        return serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
