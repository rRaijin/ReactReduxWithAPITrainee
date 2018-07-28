from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from rest_framework_jwt.views import obtain_jwt_token

from api.books.views import *


# API Registration
router = routers.DefaultRouter()
router.register(r'books', BookViewSet)

# Schema
schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('schema/', schema_view),
    path('api-token-auth/', obtain_jwt_token),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]


# if settings.DEBUG:
#     import debug_toolbar
#
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns
