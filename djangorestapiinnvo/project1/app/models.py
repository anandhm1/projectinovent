from django.db import models

class Company(models.Model):
    Company_Name = models.CharField(max_length=100,blank=False, null=False )
    Email_ID = models.EmailField(blank=False, null=False)
    Company_Code = models.CharField(max_length=100 ,unique=True,)
    Strength =models.IntegerField()
    Web_site = models.CharField(max_length=100)
    Created_time = models.DateTimeField(unique=True)

    def __str__(self):
        return self.Company_Name