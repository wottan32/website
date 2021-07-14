from django.contrib import admin
from django.http import JsonResponse
from django.urls import path
from rest_framework.templatetags.rest_framework import data
from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework import serializers
# from Datos import views
# from Datos.serializers import DatosSerializer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cliente/', JsonResponse(data, safe=False), name='Datos'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
