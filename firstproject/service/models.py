from django.db import models

from django.utils import timezone 

class Service(models.Model):
    # jo apko dynamic bnani h usko as field do
    service_icon=models.CharField(max_length=50)
    service_title=models.CharField(max_length=50)
    service_description=models.TextField()
    service_date=models.DateField(default=timezone.now)
    
# Create your models here.

