import logging

from django.contrib.auth.models import User
from rest_framework import viewsets, permissions

from back.api.user.serializers import UserSerializer, UserCreateSerializer


log = logging.getLogger(__name__)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    #TODO Temp permission
    permission_classes = (permissions.AllowAny,)

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])

    serializers = {
        'default': UserSerializer,
        'create': UserCreateSerializer,
    }
