from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

class TrendProduct(models.Model):

	name=models.CharField(max_length=200,null=True,blank=True)
	price=models.FloatField(null=True,blank=True)
	img1 = models.ImageField(upload_to='static/img/trend_img', null=True)
	img2= models.ImageField(upload_to='static/img/trend_img', null=True)
	img3 = models.ImageField(upload_to='static/img/trend_img', null=True)
	img4 = models.ImageField(upload_to='static/img/trend_img', null=True)
	title= models.CharField(max_length=200, null=True, blank=True)
	about=models.TextField(null=True,blank=True)
	color=models.CharField(max_length=200, null=True, blank=True)
	available=models.CharField(max_length=200, null=True, blank=True)
	category=models.CharField(max_length=200, null=True, blank=True)
	shipping_area=models.CharField(max_length=200, null=True, blank=True)
	shipping=models.CharField(max_length=200, null=True, blank=True)
	slug = models.SlugField(null=True,blank=True, unique=True, max_length=125)

	def save(self, *args, **kwargs):  # new
		if not self.slug:
			self.slug = slugify(self.name)
		return super().save(*args, **kwargs)
	def __str__(self):
		return self.name






