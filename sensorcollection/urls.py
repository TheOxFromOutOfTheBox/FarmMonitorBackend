from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/recv/<_device_id>',views.recvSensorData,name='recv'),
    path('api/send',views.sendSensorData,name='send'),
]