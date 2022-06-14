from django.urls import path
from .views import *
urlpatterns=[
	path('',TrendPageView,name='trend'),
	path('<slug:slug>/', TrendDetailView, name='detail_view'),

]