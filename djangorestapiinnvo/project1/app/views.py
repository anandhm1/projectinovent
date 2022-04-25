from django.shortcuts import render
from .models import Company
from .serializers import ComplanySerilizer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .paginatin import CompanyPagination
from rest_framework import generics

class CompanyDetails(APIView):


    def get(self, request):
        emp = Company.objects.all()
        serializer = ComplanySerilizer(emp, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ComplanySerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyInfo(APIView):
    def get(self, request, id):
        if id:
            try:
                emp = Company.objects.get(id=id)
            except Company.DoesNotExist:
                msg = {"msg": "Record does not exist"}
                return Response(msg, status=status.HTTP_404_NOT_FOUND)
            serializer = ComplanySerilizer(emp)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"msg": "plzz provide the id"})

    def put(self, request, id):
        if id:
            try:
                emp = Company.objects.get(id=id)
            except Company.DoesNotExist:
                msg = {"msg": "Record does not exist"}
                return Response(msg, status=status.HTTP_404_NOT_FOUND)
            serilizer = ComplanySerilizer(emp, data=request.data, partial=True)
            if serilizer.is_valid():
                serilizer.save()
                return Response(serilizer.data, status=status.HTTP_205_RESET_CONTENT)
            return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"msg": "plzz provide id"})

    def delete(self, request, id):
        if id:
            try:
                emp = Company.objects.get(id=id)
            except Company.DoesNotExist:
                msg = {"msg": "Record does not exist"}
                return Response(msg, status=status.HTTP_404_NOT_FOUND)
            emp.delete()
        return Response({"msg": "plzz provide id"})

class CompanyDtailsPagination(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = ComplanySerilizer
    pagination_class = CompanyPagination
