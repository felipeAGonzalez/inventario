from django.contrib import admin
from django.urls import path
from .common.token import CustomTokenObtainPairView, CustomTokenRefreshView
from django.urls.conf import include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Inventario API",
        default_version="v1",
        description="",
        terms_of_service="",
        contact=openapi.Contact(email=""),
        license=openapi.License(name=""),
        security=[{"Bearer":[]}],
    ),
    public=True,
    permission_classes=[]
)


# bearer_auth = openapi.SecurityRequirement(name='Bearer Token Authentication', type='apiKey', in_='header')

urlpatterns = [
        # path('swagger/', sbac chema_view.with_ui('swagger', cache_timeout=0, authentication_classes=[], permission_classes=[], security=[bearer_auth]), name='schema-swagger-ui'),

    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("admin/", admin.site.urls),
    path("api/token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", CustomTokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include("users.urls")),    
    path("api/", include("universidad.urls")),
    path("api/", include("plantel.urls")),
    path("api/", include("edificio.urls")),
    path("api/", include("aula.urls")),
    path("api/", include("dispositivo.urls")),
    path("api/", include("material.urls")),
    path("api/", include("aula_dispositivo.urls")),
    path("api/", include("dispositivo_material.urls")),
    path("api/", include("users_universidad.urls")),
]

