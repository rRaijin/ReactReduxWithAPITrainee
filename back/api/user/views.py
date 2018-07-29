from django.contrib import auth
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from back.api.user.serializers import UserSerializer, UserCreateSerializer, UserLoginSerializer
import logging

log = logging.getLogger(__name__)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])

    serializers = {
        'default': UserSerializer,
        'create': UserCreateSerializer,
        # 'update': UserUpdateSerializer,
    }


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid():
            new_data = serializer.data
            user = User.objects.get(**new_data)
            context = {
                'username': user.username,
                'id': user.id,
            }
            auth.login(request, user=user)
            log.info("User %s is logged" % data['username'])

            return Response(context)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserLogoutAPIView(APIView):
    queryset = User.objects.all()

    def get(self, request, format=None):
        log.info("User %s is logout" % request.user)
        auth.logout(request)
        return Response(status=status.HTTP_200_OK)