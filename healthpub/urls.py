from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from healthpubapi.views import register_user, login_user

from django.conf.urls import include
from rest_framework import routers
from healthpubapi.views import CustomerView
from healthpubapi.views import EmployeeView
from healthpubapi.views import SymptomView
from healthpubapi.views import AppointmentView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'customers', CustomerView, 'customer')
router.register(r'employees', EmployeeView, 'employee')
router.register(r'symptomtypes', SymptomView, 'symptom')
router.register(r'appointments', AppointmentView, 'appointment')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]