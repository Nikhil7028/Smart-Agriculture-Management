from django.contrib import admin

# Register your models here.
from .models import Officer, Scheme

# Register your models here.

class OfficerAdmin(admin.ModelAdmin):
    list_display=('id','fullName', 'mobno', 'email', 'address', 'access', 'date','password')
admin.site.register(Officer, OfficerAdmin)

# Scheme
class SchemeAdmin(admin.ModelAdmin):
    list_display=('id','title', 'titleimg', 'desc', 'officialweb', 'ytVideo', 'date', 'slug')
admin.site.register(Scheme, SchemeAdmin)
