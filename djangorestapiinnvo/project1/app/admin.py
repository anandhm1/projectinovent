from django.contrib import admin

from .models import Company
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["Company_Name","Email_ID","Company_Code","Strength","Web_site","Created_time"]
admin.site.register(Company,CompanyAdmin)
