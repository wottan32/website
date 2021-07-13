from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Datos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Datos', views.JSONResponse.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
