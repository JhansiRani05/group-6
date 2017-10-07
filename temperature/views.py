from __future__ import unicode_literals
from .models import Temperature 
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
def index(request):
	received_data=Temperature.objects.all()[len(Temperature.objects.all())-1]
	temp_data=str(received_data.tem_value)
	hum_data=str(received_data.hum_value)
	soil_data=str(received_data.soil_value)
	context={'tem':temp_data,'hum':hum_data,'soil':soil_data}
	return render(request,'temperature/index.html',context)
	
def getdata(request):
	if request.method=='GET' :
		tem_value=request.GET['temperature']
		hum_value=request.GET['humidity']
		soil_value=request.GET['soil_moisture']
                #rain_value=request.GET['rain_info']
		t_obj=Temperature()
		t_obj.tem_value=tem_value
		t_obj.hum_value=hum_value
		t_obj.soil_value=soil_value
                #t_obj.rain_value=rain_value
		t_obj.save()
		return HttpResponse("data saved in db")
	else:
		return HttpResponse("error")

def temp(request):
 received_data=Temperature.objects.all()[len(Temperature.objects.all())-1]
 temp_data=str(received_data.tem_value)
 hum_data=str(received_data.hum_value)
 context={'tem':temp_data,'hum':hum_data}
 return render(request,'temperature/temp.html',context)
 
def micro(request):
 received_data=Temperature.objects.all()[len(Temperature.objects.all())-1]
 soil_data=str(received_data.soil_value)
 #rain_data=str(received_data.rain_info)
 context={'soil':soil_data}
 return render(request,'temperature/micro.html',context)

def aa():
 received_data=Temperature.objects.all()[len(Temperature.objects.all())-1]
 soil_data=str(received_data.soil_value)
 return soil_data
 
