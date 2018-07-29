import logging

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
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
    confirm_password = serializers.CharField(label='Confirm password',
                                             write_only=True,
                                             style={'input_type': 'password'})

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'confirm_password',
            'email',
        )

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.pop('confirm_password')
        if password != confirm_password:
            raise ValidationError('Passwords do not match')
        return data

    def create(self, validated_data):
        password = validated_data.get("password")
        username = validated_data.get("username")
        email = validated_data.get("email")
        try:
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            user.save()
            log.info("User %s, %s successfully created" % (user.username, user.email))
            log.info("User obtained token %s" % token)
            return user
        except Exception as e:
            return e


class UserLoginSerializer(ModelSerializer):
    username = serializers.CharField(allow_blank=True)
    password = serializers.CharField(allow_blank=False, write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]

    def validate(self, data):
        user_obj = None
        username = data['username']
        password = data['password']
        if not username:
            raise ValidationError('Username is required to login.')
        user = User.objects.filter(username=username).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError('This username is not valid.')

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError('Password is incorrect. Try again.')
            if not username:
                username = user_obj.username
        data['username'] = username
        return data