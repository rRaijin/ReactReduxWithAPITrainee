from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from back.api.book.views import *
from back.api.user.views import *


# API Registration
router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'users', UserViewSet)

# Schema
schema_view = get_swagger_view(title='Pastebin API')

from rest_framework import views, serializers, status
from rest_framework.response import Response

class MessageSerializer(serializers.Serializer):
    message = serializers.CharField()
class EchoView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED)

urlpatterns = [
    path('api/auth', include('rest_framework.urls', namespace='rest_framework')),
    path('api/auth/token/obtain', TokenObtainPairView.as_view()),
    path('api/auth/token/refresh', TokenRefreshView.as_view()),
    path('api/echo/', EchoView.as_view()),
    path('schema/', schema_view),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]


# if settings.DEBUG:
#     import debug_toolbar
#
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns
