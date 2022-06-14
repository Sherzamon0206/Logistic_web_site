from django.urls import path
from .views import *
urlpatterns=[
    path('',CalculatorPageView,name='calculator'),
    path('calculator/',Calculator,name='name'),
    path('company/',CompanySendFunc,name="company"),
    path('saqlash/',Saqlash,name="saqlash"),



]