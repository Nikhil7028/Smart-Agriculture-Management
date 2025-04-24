# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
import requests
from django.http import JsonResponse
from .models import FarmerInfo, worker
from office.models import Scheme
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
    countFarmer= FarmerInfo.objects.count()
    available_workers = worker.objects.filter(availabillity=True).count()
    top5_schemes = Scheme.objects.order_by('-id')[:5] 
    count={'registerFarmer':countFarmer, 'availableWorker': available_workers,'top5_schemes':top5_schemes}
    # print(count)
    return render(request, 'index.html', count)

def weather(request):
    return render(request, 'weather.html')

def GovermentScheme(request):
    return render(request, 'GovermentSchem.html')


def AvailableLaborers(request):
    if request.method == 'POST':
        Selectdistrict = request.POST.get('district')
        if Selectdistrict:
            SelectSubd = request.POST.get('subDist')
            if SelectSubd:
                selectVillage = request.POST.get('village')
                if selectVillage:
                    workers = worker.objects.filter(
                        availabillity=True,
                        village=selectVillage,
                        subDist=SelectSubd,
                        dist=Selectdistrict
                    )
                    return render(
                        request, 'available-laborers.html',
                        {'Selectdistrict':Selectdistrict,'SelectSubd':SelectSubd,
                         'SelectVillage':selectVillage, 'workers': workers}
                    )
                else:   # if village is not selected only dist and sub-dist
                    workers = worker.objects.filter(
                        availabillity=True,
                        subDist=SelectSubd,
                        dist=Selectdistrict
                    )
                    distinctVillage = worker.objects.filter(availabillity=True, dist=Selectdistrict, subDist=SelectSubd).values_list('village', flat=True).distinct()
                    return render(
                        request, 'available-laborers.html',
                        {'Selectdistrict':Selectdistrict,'SelectSubd':SelectSubd,
                         'options':distinctVillage,
                         'workers': workers}
                    )
            else:    #only select dist
               workers = worker.objects.filter(availabillity=True, dist=Selectdistrict)
               distinctSubd = worker.objects.filter(availabillity=True, dist=Selectdistrict).values_list('subDist', flat=True).distinct()
               print(distinctSubd)
               return render(request, 'available-laborers.html',{'Selectdistrict':Selectdistrict, 'options':distinctSubd, 'workers': workers})
    districts = worker.objects.values_list('dist', flat=True).distinct()
    return render(request, 'available-laborers.html',{'dist':districts})



def schemeDetail(request, slug):
    scheme = get_object_or_404(Scheme, slug=slug)
    return render(request, 'SchemeDetail.html', {'scheme': scheme})


def farmerRegistration(request):
    if request.method == 'POST':
        try: 
            fullname = request.POST.get('fullName')
            mobno = request.POST.get('phone')
            whatappsno = request.POST.get('whatsapp')
            email = request.POST.get('email')
            gender = request.POST.get('gender')
            village = request.POST.get('village').capitalize()
            dist = request.POST.get('dist').capitalize()
            subdistrict = request.POST.get('subdistrict').capitalize()
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
            dist = request.POST.get('dist').capitalize()
            subdist = request.POST.get('sub_district').capitalize()
            village = request.POST.get('village').capitalize()
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
            notify= f"Form not submitted {e}"
        return render (request, 'worker_registration.html',{'cls':cls,'status': status, 'msg': notify})
    return render(request, 'worker_registration.html')







