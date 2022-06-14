from django.shortcuts import render
from .models import *
import json
from django.http import JsonResponse

import requests

def TrendPageView(request):
	DATA = TrendProduct.objects.all()

	return render(request=request, template_name='trend.html', context={"products": DATA})
def TrendDetailView(request,slug):

	CHECK=TrendProduct.objects.get(slug=slug)




	return render(request=request, template_name='product.html', context={"detail": CHECK })


