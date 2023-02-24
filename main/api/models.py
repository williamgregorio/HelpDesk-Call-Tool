from django.db import models

# Create your models here.

class Log(models.Model):
    name = models.CharField(max_length=30 default='')
    call_back_number = models.IntegerField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    problem = models.CharField(max_length=250 default='')
    solution = models.CharField(max_length=250 default='')
    incident_number = models.IntegerField(null=False, blank=False)
    created_at = models.DateField(auto_now_add=True)

