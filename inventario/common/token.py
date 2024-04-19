from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.models import Users


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom TokenObtainPairSerializer.

    This class is used to customize the claims of the JWT Token.
    """

    @classmethod
    def get_token(cls, users: Users):
        """
        Override the get_token method to add custom claims to the JWT Token.

        Args:
            user: The user object.
        """
        token = super().get_token(users)
        groups = [i.name for i in users.groups.all()]
        token["username"] = users.username
        token["email"] = users.email
        token["groups"] = groups
        return token


@method_decorator(name="post", decorator=swagger_auto_schema(tags=["core/token"]))
class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom TokenObtainPairView.

    A custom view is needed to be able to override the serializer_class and use
    our CustomTokenObtainPairSerializer, as well as to generate the proper
    endpoints in swagger.
    """

    serializer_class = CustomTokenObtainPairSerializer


@method_decorator(name="post", decorator=swagger_auto_schema(tags=["core/token"]))
class CustomTokenRefreshView(TokenRefreshView):
    """
    Custom TokenRefreshView.

    A custom view is needed to be able to generate the proper endpoints in
    swagger.
    """
