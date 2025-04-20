# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect, render
import requests
from django.http import JsonResponse
from .models import FarmerInfo, worker
# Load model once globally
# views.py
import os
import joblib
model_path = os.path.join(os.path.dirname(__file__), 'ml_model/crop_recommendation_model.pkl')
model = joblib.load(model_path)

def RecommendCrop(request):
    result = None
    if request.method == 'POST':
        try:
            nitrogen = float(request.POST.get('nitrogen'))
            phosphorous = float(request.POST.get('phosphorous'))
            potassium = float(request.POST.get('potassium'))
            temperature = float(request.POST.get('temperature'))
            humidity = float(request.POST.get('humidity'))
            ph = float(request.POST.get('ph'))
            rainfall = float(request.POST.get('rainfall'))

            input_data = [[nitrogen, phosphorous, potassium, temperature, humidity, ph, rainfall]]
            result = model.predict(input_data)[0]
        except Exception as e:
            result = f"Error: {str(e)}"

    return render(request, 'recommend_crop.html', {'result': result})

def home(request):
    return render(request, 'index.html')

def weather(request):
    return render(request, 'weather.html')

def GovermentScheme(request):
    return render(request, 'GovermentSchem.html')

# def AvailableLaborers(request):
#     return render(request, 'available-laborers.html')
# def AvailableLaborers(request):
#     workers = worker.objects.filter(availabillity=True)
#     print(worker)
#     return render(request, 'available-laborers.html', {'workers': workers})




def schemeDetail(request):
    return render(request, 'SchemeDetail.html')


def farmerRegistration(request):
    if request.method == 'POST':
        try: 
            fullname = request.POST.get('fullName')
            mobno = request.POST.get('phone')
            whatappsno = request.POST.get('whatsapp')
            email = request.POST.get('email')
            gender = request.POST.get('gender')
            village = request.POST.get('village')
            dist = request.POST.get('dist')
            subdistrict = request.POST.get('subdistrict')
            pincode = request.POST.get('pincode')
            landSize = request.POST.get('landSize')
            cropType = request.POST.get('cropType')
            irrigation = request.POST.get('irrigation')

            FarmerInfo.objects.create( fullname=fullname, mobno=mobno, whatappsno=whatappsno,
                email=email,   gender=gender,                village=village, dist=dist,      subdist=subdistrict,                pincode=pincode,                totalland=landSize,                maincrop=cropType,                irrigation=irrigation,
            )
            cls='success'
            status="Sucessfully"
            notify= "Your form has been submitted sucessfully"
        except Exception as e:
            print(f"Error: {e}")
            cls='danger'
            status="ERROR"
            notify= "Form not submitted {e}"
        return render (request, 'F_registration.html',{'cls':cls,'status': status, 'msg': notify})
    
    return render(request, 'F_registration.html')

def workerRegistration(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            age = request.POST.get('age')
            gender = request.POST.get('gender')
            dist = request.POST.get('dist')
            subdist = request.POST.get('sub_district')
            village = request.POST.get('village')
            phone = request.POST.get('mobno')
            skills = request.POST.get('skills')
            availability = request.POST.get('availability')
            availability = True if availability == 'True' else False

            worker.objects.create(
                fullName=name,                age=age,
                gender=gender,                dist=dist,
                subDist= subdist,                village=village,
                mobno=phone,                skill=skills,      
                availabillity=availability
            )
            cls='info'
            status="Sucessfully"
            notify= "Your form has been submitted sucessfully"
        except Exception as e:
            print(f"Error: {e}")
            cls='danger'
            status="ERROR"
            notify= "Form not submitted {e}"
        return render (request, 'worker_registration.html',{'cls':cls,'status': status, 'msg': notify})
    return render(request, 'worker_registration.html')

