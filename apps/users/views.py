from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken

from apps.users.serializers import UserSerializer, AuthTokenSerializer
from .models import User


class CreateUserview(generics.CreateAPIView):
    '''
    Vista para registrar un usuario
    '''
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class RetrieveUpdateUserView(generics.RetrieveUpdateAPIView):
    '''
    Vista para ver y actualizar total o parcialmente el usuario logueado.
    '''
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class CreateTokenView(ObtainAuthToken):
    '''
        Vista para crear un token
    '''
    serializer_class = AuthTokenSerializer


class ListUserView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
