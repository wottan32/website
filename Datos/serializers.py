from rest_framework import serializers
from .models import Datos


# from datetime import datetime
# from django.utils import timezone
# from django.utils.six import BytesIO
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser

class DatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datos
        fields = '__all__'
        # fields = ('id', 'nombre')
