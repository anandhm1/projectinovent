from django.db import models

from django.core.validators import RegexValidator


alphanumeric = RegexValidator(r'^[a-zA-Z]{2}*[0-9]{2}*[E|N]{1}*$', )

class Company(models.Model):
    Company_Name = models.CharField(max_length=100,blank=False, null=False )
    Email_ID = models.EmailField(blank=False, null=False)
    Company_Code = models.CharField(max_length=100 ,unique=True,validators=[alphanumeric])
    Strength =models.IntegerField()
    Web_site = models.CharField(max_length=100)
    Created_time = models.DateTimeField(unique=True)

