from django.shortcuts import render, redirect
from office.models import Officer
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
   return render(request, 'office/officeDashboard.html')

def f_logout(request):
    if 'officeemail' in request.session:
        del request.session['officeemail']    
    # Redirect to the login page after logging out
    return redirect('office_login') 
    