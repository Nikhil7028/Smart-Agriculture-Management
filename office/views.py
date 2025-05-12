from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render, redirect
from office.models import Officer, Scheme
from agri.models import worker, FarmerInfo, HireRequest
from django.db.models import Count

# Create your views here.
def officeLogin(request):
  if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Find the user by email
            user = Officer.objects.get(email=email)

            # Check if the password matches
            if password == user.password:  # If passwords match
                if user.access:  # Check if the user has access = True
                    request.session['officeemail'] = email
                    return redirect('office_home')  # Redirect to the 'office_home' page
                else:
                    txt = 'warning'
                    content = "Access denied! Your account is inactive."
            else:
                txt = 'danger'
                content = "Invalid username and password"
        
        except Officer.DoesNotExist:
            txt = 'danger'
            content = "Invalid username and password"
        
        except Exception as e:
            print(f"Error: {e}")
            txt = 'danger'
            content = f"Form not submitted: {e}"

        # Render the login page with the error or success message
        return render(request, 'office/officeLogin.html', {'txt': txt, 'content': content})
  return render(request, 'office/officeLogin.html')
    
def officeDashboard(request):
   countFarmer= FarmerInfo.objects.count()
   avlWorker = worker.objects.filter(availabillity=True).count()
   avlNot = worker.objects.count() - avlWorker
   countScheme = Scheme.objects.count()
   return render(request, 'office/officeDashboard.html',{'famer': countFarmer, 'worker_yes': avlWorker, 'worker_no':avlNot,'scheme':countScheme, 'ttl': avlWorker+avlNot})

def f_logout(request):
    if 'officeemail' in request.session:
        del request.session['officeemail']    
    # Redirect to the login page after logging out
    return redirect('office_login') 
    
def addScheme(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        title_img = request.FILES.get('title_image')
        description = request.POST.get('description')
        official_link = request.POST.get('official_link')
        yt_link = request.POST.get('youtube_link')
        
        try:
            Scheme.objects.create( title=title, titleimg= title_img, desc=description, officialweb= official_link, ytVideo= yt_link  );
            cls='sucess'
            status="Sucessfully"
            notify= "Scheme added sucessfully"
        except Exception as e:
            print(f"Error: {e}")
            cls='danger'
            status="ERROR"
            notify= f"Form not submitted {e}"
        allScheme= Scheme.objects.all()
        
        dict={
            'cls':cls,'status': status, 'msg': notify, 'Schemes': allScheme
        }
        return render(request, 'office/addScheme.html',dict)
    allScheme= Scheme.objects.all().order_by('-id')

    countScheme= allScheme.count()
    return render(request, 'office/addScheme.html',{'Schemes': allScheme, 'totalScheme': countScheme })

def delete_scheme(request, id):
    scheme = get_object_or_404(Scheme, id=id)
    scheme.delete()
    return redirect('add_sheme')

def editProfile(request):
    if 'officeemail' not in request.session:  # Check if the session is set
        return redirect('office_login')  # Redirect to the login page if session is not set

    office_email = request.session.get('officeemail')
    cls = status = notify =None
    
    if request.method == 'POST':
        try:
        # Get data from the form
            profile = Officer.objects.get(email=office_email)  # Fetch the profile using the email from session
            full_name = request.POST.get('name')
            mobno = request.POST.get('mobno')
            address = request.POST.get('address')
            
            # Update the profile
            profile.fullName = full_name
            profile.mobno = mobno
            profile.address = address
            profile.save()  # Save the updated profile
            cls='Successfully!'
            status="Updated"
            notify= "Your profile is updated Successfully"
        except Exception as e:
            print(f"Error: {e}")
            cls='danger'
            status="ERROR!"
            notify= f"Your profile is not updated {e}"
    profile = Officer.objects.get(email=office_email)
    return render(request, 'office/editProfile.html', {'user': profile, 'cls':cls, 'status':status, 'notify':notify})

def changePassword(request):
    if 'officeemail' not in request.session:  # Check if the session is set
        return redirect('office_login')
    if request.method == 'POST':
        newPass= request.POST.get('newPassword')
        confPass= request.POST.get('confirmNewPassword')
        prevPass= request.POST.get('prevPassword')
        
        try:
            office_email = request.session.get('officeemail')
            profile = Officer.objects.get(email=office_email)
            if profile.password == prevPass:
                profile.password= newPass
                profile.save()
                cls='success'
                status="Update!"
                notify= "Password change Sucessfully"

            else:
                cls='warning'
                status="Password not change!"
                notify= "wrong previous pass"
        except Exception as e:
                print(e)
                cls='danger'
                status="ERROR!"
                notify= f"Password is not change {e}"
        return render(request, 'office/changePassword.html', {'cls':cls, 'status':status, 'notify':notify})
    
    return render(request, 'office/changePassword.html')



# def report_view(request):
#     # Count distinct farmers who have made at least one request
#     total_farmers = HireRequest.objects.values('farmer').distinct().count()

#     # Count distinct workers who have received at least one request
#     total_workers = HireRequest.objects.values('worker').distinct().count()

#     # Optional: Total hire requests
#     total_requests = HireRequest.objects.count()

#     # Optional: How many times each worker has been hired
#     worker_hire_counts = HireRequest.objects.values('worker__fullName').annotate(total=Count('id'))

#     context = {
#         'total_farmers': total_farmers,
#         'total_workers': total_workers,
#         'total_requests': total_requests,
#         'worker_hire_counts': worker_hire_counts,
#     }
#     return render(request, 'office/report.html', context)


# def report_view(request):
#     start_date = request.GET.get('start_date')
#     end_date = request.GET.get('end_date')

#     hire_requests = HireRequest.objects.all()

#     if start_date:
#         hire_requests = hire_requests.filter(hire_date__date__gte=start_date)
#     if end_date:
#         # Include the entire end day by adding 1 day and subtracting a second
#         hire_requests = hire_requests.filter(hire_date__date__lte=end_date)
        
#     worker_hire_counts = hire_requests.values('worker__fullName', 'farmer').annotate(total=Count('id'))


#     context = {
#         'worker_hire_counts': worker_hire_counts,
#         'total_farmers': hire_requests.values('farmer').distinct().count(),
#         'total_workers': hire_requests.values('worker').distinct().count(),
#         'total_requests': hire_requests.count(),
#     }

#     return render(request, 'office/report.html', context)

def report_view(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    hire_requests = HireRequest.objects.all()

    if start_date:
        hire_requests = hire_requests.filter(hire_date__date__gte=start_date)
    if end_date:
        hire_requests = hire_requests.filter(hire_date__date__lte=end_date)

    context = {
        'hire_requests': hire_requests.order_by('-hire_date'),  # show latest first
        'total_farmers': hire_requests.values('farmer').distinct().count(),
        'total_workers': hire_requests.values('worker').distinct().count(),
        'total_requests': hire_requests.count(),
    }

    return render(request, 'office/report.html', context)

