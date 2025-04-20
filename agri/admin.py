from django.contrib import admin
from .models import FarmerInfo, worker

# Register your models here.
class famerAdmin(admin.ModelAdmin):
    list_display=('id','fullname', 'whatappsno', 'email', 'gender', 'village', 'dist', 'subdist', 'pincode', 'totalland', 'maincrop', 'irrigation' , 'date')
admin.site.register(FarmerInfo, famerAdmin)

# Register worker model
class workerAdmin(admin.ModelAdmin):
    list_display=('id','fullName', 'age', 'gender', 'dist', 'subDist', 'village','mobno', 'skill', 'availabillity','date' )
admin.site.register(worker, workerAdmin)
