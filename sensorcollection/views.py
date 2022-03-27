from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import SensorData
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def index(request):
    return HttpResponse("Hello man im at index page.")

@csrf_exempt
def sendSensorData(request):
    if(request.method=='POST'):
        data = json.loads(request.body)
        print(data)
        SensorData.objects.create(
            device_id = data["device_id"],
            temperature = data["temperature"],
            soil_moisture = data["soil_moisture"],
            humidity = data["humidity"],
        )
        return JsonResponse({'Success':"Created"})
    return JsonResponse({'Error':'Method Allowed only POST'})

def recvSensorData(request,_device_id):
    obj=SensorData.objects.filter(device_id=_device_id)[:15]
    print(obj)
    res=[]
    for each in obj:
        temp = {}
        temp['device_id'] = each.device_id
        temp['humidity'] = each.humidity
        temp['temperature'] = each.temperature
        temp['soil_moisture'] = each.soil_moisture
        temp['timestamp'] = each.timestamp        

        res.append(temp)
    return JsonResponse({'data':res})


