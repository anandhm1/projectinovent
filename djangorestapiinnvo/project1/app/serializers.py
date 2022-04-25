from .models import Company
from rest_framework import serializers


class ComplanySerilizer(serializers.ModelSerializer):
    class Meta:
      model = Company
      fields = "__all__"


    def validate_Company_Name(self,value):
      value1 = len(value)
      print(value1)
      if value1<5:
          raise serializers.ValidationError("Comapany Name should not less than 5 characters")
      return value


