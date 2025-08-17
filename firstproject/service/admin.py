from django.contrib import admin
from service.models import Service
class ServiceAdmin(admin.ModelAdmin):
    list_dis=['service_icon','service_title','service_description','service_date']


# Register your models here.
admin.site.register(Service,ServiceAdmin)