from django.contrib import admin
from .models import FarmerInfo, worker, contactUs, HireRequest

# Register your models here.
class famerAdmin(admin.ModelAdmin):
    list_display=('id','fullname', 'whatappsno', 'email', 'gender', 'village', 'dist', 'subdist', 'pincode', 'totalland', 'maincrop', 'irrigation','password' , 'date')
admin.site.register(FarmerInfo, famerAdmin)

# Register worker model
class workerAdmin(admin.ModelAdmin):
    list_display=('id','fullName', 'age', 'gender', 'dist', 'subDist', 'village','mobno', 'skill', 'availabillity','password','date' )
admin.site.register(worker, workerAdmin)

class contactAdmin(admin.ModelAdmin):
    list_display=('id','Name', 'email', 'phone', 'message','checked', 'date')
admin.site.register(contactUs, contactAdmin)


class RequestAdmin(admin.ModelAdmin):
    list_display=('id','worker', 'purpose','farmer', 'duration','f_mobno', 'location','STATUS', 'hire_date')
admin.site.register(HireRequest, RequestAdmin)


