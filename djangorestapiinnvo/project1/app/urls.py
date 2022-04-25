from .views import CompanyDetails,CompanyInfo,CompanyDtailsPagination
from django.urls import path

urlpatterns = [
    path("details/",CompanyDetails.as_view()),
    path("details/<int:id>/",CompanyInfo.as_view()),
    path("pagination/",CompanyDtailsPagination.as_view())

]