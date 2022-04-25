from .models import Company
from rest_framework import serializers
import re

class ComplanySerilizer(serializers.ModelSerializer):
    class Meta:
      model = Company
      fields = "__all__"


    def validate_Company_Name(self,value):
      value1 = len(value)
      print(value1)
      if value1>5:
          raise serializers.ValidationError("Comapany Name should not less than 5 characters")
      return value

    def validate_Company_Code(self,value):
        value1 = len(value)
        valid_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        number = "0123456789"
        vali = "EN"
        v1=value[0:2]
        v2=value[2:4]
        v3=value[4:5]

        print(v1,v2,v3)

        if value1 != 5:
               raise serializers.ValidationError("Comapany code should equle to 5 characters")
        for i in v1:
                if i not in valid_characters:
                    raise serializers.ValidationError("Comapany code should 2 characters only ")
        for i in v2:
                if i not in number:
                    raise serializers.ValidationError("Comapany code should  2 number only ")
        for i in v3:
            if i not in vali:
                raise serializers.ValidationError("Comapany code at lest one Character is E OR N ")

        return value

