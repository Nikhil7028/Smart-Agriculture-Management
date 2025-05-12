# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
import requests
from django.http import JsonResponse
from .models import FarmerInfo, worker, contactUs, HireRequest
from office.models import Scheme
# Load model once globally
# views.py
import os
import joblib
model_path = os.path.join(os.path.dirname(__file__), 'ml_model/crop_recommendation_model.pkl')
model = joblib.load(model_path)


# dataDictionary
fertilizer_suggestions = {
    'Rice': 'Urea, DAP, Potash',
    'Wheat': 'Nitrogen, Phosphate, Potassium',
    'Cotton': 'Zinc sulfate, Urea, MOP',
    'Maize': 'NPK, Zinc, Boron',
    'Barley': 'Phosphorus, Potassium, Nitrogen',
    'Sugarcane': 'Urea, Potash, Zinc sulfate',
    'Tomato': 'NPK, Calcium nitrate, Super phosphate',
    'Potato': 'Urea, NPK, Zinc sulfate',
    'Peas': 'Phosphate, Potassium, Calcium',
    'Chili': 'Urea, Potash, DAP',
    'Carrot': 'NPK, Calcium nitrate, Magnesium sulfate',
    'Soybean': 'Urea, Potash, Phosphorus',
    'Groundnut': 'Urea, Super phosphate, MOP',
    'Mustard': 'Urea, NPK, Zinc',
    'Brinjal': 'NPK, Potash, Zinc',
    'Onion': 'Urea, Super phosphate, MOP',
    'Garlic': 'Urea, Potash, Zinc',
    'Cucumber': 'NPK, Urea, Magnesium sulfate',
    'Lettuce': 'NPK, Calcium nitrate, Phosphorus',
    'Watermelon': 'NPK, Urea, Potash'
    }

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

# def home(request):
#     countFarmer= FarmerInfo.objects.count()
#     available_workers = worker.objects.filter(availabillity=True).count()
#     top5_schemes = Scheme.objects.order_by('-id')[:5] 
#     count={'registerFarmer':countFarmer, 'availableWorker': available_workers,'top5_schemes':top5_schemes}
#     # print(count)
#     return render(request, 'index.html', count)

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Save to database
        contactUs.objects.create(Name=name, email=email, phone=phone, message=message)
        print('ok')

        return redirect('home')  # Replace with your actual URL name

    # Data for homepage
    countFarmer = FarmerInfo.objects.count()
    available_workers = worker.objects.filter(availabillity=True).count()
    top5_schemes = Scheme.objects.order_by('-id')[:5]
    count = {
        'registerFarmer': countFarmer,
        'availableWorker': available_workers,
        'top5_schemes': top5_schemes
    }
    return render(request, 'index.html', count)

def weather(request):
    return render(request, 'weather.html')

def GovermentScheme(request):
    allScheme = Scheme.objects.all().order_by('-id')    
    return render(request, 'GovermentSchem.html',{'schemes': allScheme})

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
            password = request.POST.get('newPassword')
            availability = request.POST.get('availability')
            availability = True if availability == 'True' else False

            worker.objects.create(
                fullName=name,                age=age,
                gender=gender,                dist=dist,
                subDist= subdist,                village=village,
                mobno=phone,                skill=skills, 
                password=password,     
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

def workerLogin(request):
    if request.method == 'POST':
        Mobno = request.POST.get('mobno')
        password = request.POST.get('password')
        try:
            # Find the worker by phone number
            user = worker.objects.get(mobno=Mobno)

            # Check if the password matches
            if password == user.password:
                request.session['workerName'] = user.fullName
                request.session['workerMobno'] = Mobno
                return redirect('worker_home')  # Redirect to 'worker_home' page

            else:
                txt = 'danger'
                content = "Invalid mobile number or password"

        except worker.DoesNotExist:
            txt = 'danger'
            content = "Invalid mobile number or password"

        except Exception as e:
            print(f"Error: {e}")
            txt = 'danger'
            content = f"Form not submitted: {e}"

        # Render the login page with error message
        return render(request, 'workerLogin.html', {'txt': txt, 'content': content})

    return render(request, 'workerLogin.html')

def workerDashboard(request):
    try:
        worker_name = request.session.get('workerName')
        worker_mobno = request.session.get('workerMobno')

        if not worker_name or not worker_mobno:
            return redirect('worker_login')

        # Get the worker object
        worker_obj = worker.objects.get(mobno=worker_mobno)
        message=None
        if request.method == 'POST':
            # Get the checkbox value from the form
            availability_value = request.POST.get('availability')
            # Checkbox sends 'on' when checked, nothing when unchecked
            worker_obj.availabillity = True if availability_value == 'on' else False
            worker_obj.save()
            message='Availability status updated'
            # Optionally, you can set a success message here

        return render(request, 'worker/workerDashboard.html', {'status': worker_obj.availabillity, 'msg': message })

    except worker.DoesNotExist:
        request.session.flush()
        return redirect('worker_login')

    except Exception as e:
        print(f"Error: {e}")
        return redirect('worker_login')

def w_logout(request):
    if 'workerMobno' in request.session:
        del request.session['workerMobno']    
        del request.session['workerName']    
    # Redirect to the login page after logging out
    return redirect('worker_login') 
  
def fertilizer_suggestion_view(request):
    
    selected_crop = None
    suggestion = None

    if request.method == 'POST':
        selected_crop = request.POST.get('crop')
        suggestion = fertilizer_suggestions.get(selected_crop, 'No suggestion available for this crop.')

    return render(request, 'fertilizer_suggestion.html', {
        'fertilizer_suggestions': fertilizer_suggestions,
        'selected_crop': selected_crop,
        'suggestion': suggestion
    })



def hire_worker(request, worker_id):
    print('hi')
    work = get_object_or_404(worker, id=worker_id)
    print(request.method)
    

    # if request.method == 'POST':
    #     purpose = request.POST.get('purpose')
    #     duration = request.POST.get('duration')
    #     location = request.POST.get('location')
    #     farmer_name = request.POST.get('fname')
    #     mobile_number = request.POST.get('fmob')
        
    #     print("DEBUG:", farmer_name, purpose, duration, location, mobile_number)

    #     # Save to the database
    #     HireRequest.objects.create(
    #         farmer=farmer_name,
    #         worker=work,
    #         purpose=purpose,
    #         duration=duration,
    #         location=location,
    #         f_mobno=mobile_number
    #     )

    #     return render(request, 'hire_request.html', {
    #         'worker': work, 'success': True
    #     })
    if request.method == 'POST':
        purpose = request.POST.get('purpose')
        duration = request.POST.get('duration')
        location = request.POST.get('location')
        farmer_name = request.POST.get('fname')
        mobile_number = request.POST.get('fmob')

        if all([purpose, duration, location, farmer_name, mobile_number]):
            HireRequest.objects.create(
                farmer=farmer_name,
                worker=work,
                purpose=purpose,
                duration=duration,
                location=location,
                f_mobno=mobile_number
            )
            return render(request, 'hire_request.html', {
                'worker': work,
                'success': True
            })
        else:
            return render(request, 'hire_request.html', {
                'worker': work,
                'success': False
            })

    return render(request, 'hire_request.html', { 'worker': work })


def acceptRequest(request):
    workerMob = request.session.get('workerMobno')

    # Get the worker instance
    worker_instance = get_object_or_404(worker, mobno=workerMob)

    # if request.method == 'POST':
    #     req_id = request.POST.get('req_id')  # Get request ID from hidden field
    #     new_status = request.POST.get('status')

    #     # Get the specific hire request
    #     hire_request = get_object_or_404(HireRequest, id=req_id, worker=worker_instance)
    #     hire_request.STATUS = new_status
    #     hire_request.save()

        # Optional: Add a success message or redirect if you want

    # Fetch all requests for this worker to display in the table
    hire_requests = HireRequest.objects.filter(worker=worker_instance).order_by('-hire_date')

    return render(request, 'worker/AcceptRequest.html', {
        'hire_requests': hire_requests
    })


def update_request_status(request, req_id):
    if request.method == 'POST':
        new_status = request.POST.get('status')
        hire_request = get_object_or_404(HireRequest, id=req_id)
        hire_request.STATUS = new_status
        hire_request.save()
    return redirect('accept_request')