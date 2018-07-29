from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from rest_framework_jwt.views import obtain_jwt_token

from back.api.book.views import *
from back.api.user.views import *


# API Registration
router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'users', UserViewSet)

# Schema
schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name="login"),
    path('logout/', UserLogoutAPIView.as_view(), name="logout"),
    path('schema/', schema_view),
    path('obtain-token/', obtain_jwt_token),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]


# if settings.DEBUG:
#     import debug_toolbar
#
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns
