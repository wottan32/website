import json_response
from django.shortcuts import render
from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.request import Request
import requests
# from rest_framework import status
# from .models import Datos
# from .serializers import DatosSerializer
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
# from datetime import datetime
# from django.utils import timezone
# from django.utils.six import BytesIO
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser

from rest_framework.permissions import IsAuthenticated

# from django.http import HttpResponse


# from django.shortcuts import get_object_or_404

# Lists all stocks or create a new one
# stocks/

class DatosView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(request):
        url = "https://api.chipax.com/clientes"
        headers = {'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTExMiwiZXhwaXJhdGlvbiI6MTYyNTA4Mjg0MSwiaWF0IjoxNjI1MDc5MjQxfQ.T5OSbqrS5j2GoOZCUI2cVrkwcAdLQUQI6de3hEq8Vbg'}
        response = requests.get(url, headers=headers)

        return render(request, json_response)


'''      
        geodata = response.json()
        return render(request, 'core/home.html', {
            'ip': geodata['ip'],
            'country': geodata['country_name']
        })

class DatosView(APIView):

    def get(self, request):
        queryset = Datos.objects.all()
        serializer = DatosSerializer(Datos, many=True)
        return Response(serializer.data)

    def post(self):
        pass



class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

    @classmethod
    def as_view(cls):
        pass


@csrf_exempt
def Datos_list(request):
    if request.method == 'GET':
        datos = Datos.objects.all()
        datos_serializer = DatosSerializer(datos, many=True)
        return JSONResponse(datos_serializer.data)

    elif request.method == 'POST':
        datos_data = JSONParser().parse(request)
        datos_serializer = DatosSerializer(data=datos_data)
        if datos_serializer.is_valid():
            datos_serializer.save()
            return JSONResponse(datos_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JSONResponse(datos_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

'''
