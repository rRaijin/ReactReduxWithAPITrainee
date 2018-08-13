import logging

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

log = logging.getLogger(__name__)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
        )


class UserCreateSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(label='Password',
                                     write_only=True,
                                     style={'input_type': 'password'})

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )

    def create(self, validated_data):
        password = validated_data.get("password")
        username = validated_data.get("username")
        try:
            user = User.objects.create(username=username)
            user.set_password(password)
            user.save()
            log.info("User %s, %s successfully created" % (user.username, user.email))
            return user
        except Exception as e:
            print(e)
            return e
