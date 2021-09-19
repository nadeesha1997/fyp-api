from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from upload.models import Value,Sensor,Device,Reading
from upload.serializer import ValueSerializer,SensorSerializer,DeviceSerializer,ReadingSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def dataupload(request,id='0'):
    if request.method=='GET':
        readings=Reading.objects.all()
        readings_serializer=ReadingSerializer(readings,many=True)
        return JsonResponse(readings_serializer.data,safe=False)
    elif request.method=='POST':
        readings_data=JSONParser().parse(request)
        readings_serializer=ReadingSerializer(data=readings_data)
        if readings_serializer.is_valid():
            readings_serializer.save()
            return JsonResponse("Added sucessfully",safe=False)
        return JsonResponse("Failed to add",safe=False)
    elif request.method=='PUT':
        readings_data = JSONParser().parse(request)
        readings = Reading.objects.get(reading_id=readings_data['reading_id'])
        reading_serializer=ReadingSerializer(readings,data=readings_data)
        if reading_serializer.is_valid():
            reading_serializer.save()
            return JsonResponse("Update successfull",safe=False)
        return JsonResponse("Update failed",safe=False)
    elif request.method=='DELETE':
        reading=Reading.objects.get(reading_id=id)
        reading.delete()
        return JsonResponse("Delete successfull",safe=False)

@csrf_exempt
def dataupload(request,id='0'):
    if request.method=='GET':
        readings=Reading.objects.all()
        readings_serializer=ReadingSerializer(readings,many=True)
        return JsonResponse(readings_serializer.data,safe=False)
    elif request.method=='POST':
        readings_data=JSONParser().parse(request)
        readings_serializer=ReadingSerializer(data=readings_data)
        if readings_serializer.is_valid():
            readings_serializer.save()
            return JsonResponse("Added sucessfully",safe=False)
        return JsonResponse("Failed to add",safe=False)
    elif request.method=='PUT':
        readings_data = JSONParser().parse(request)
        readings = Reading.objects.get(reading_id=readings_data['reading_id'])
        reading_serializer=ReadingSerializer(readings,data=readings_data)
        if reading_serializer.is_valid():
            reading_serializer.save()
            return JsonResponse("Update successfull",safe=False)
        return JsonResponse("Update failed",safe=False)
    elif request.method=='DELETE':
        reading=Reading.objects.get(reading_id=id)
        reading.delete()
        return JsonResponse("Delete successfull",safe=False)