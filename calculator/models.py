from django.db import models


class Country(models.Model):

    country=models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.country



class Company(models.Model):

    company_name=models.CharField(max_length=200,null=True,blank=True)
    company_logo=models.ImageField(upload_to="img")
    company_type=models.CharField(max_length=200,null=True,blank=True)
    days=models.CharField(max_length=10,null=True,blank=True)

    kg05=models.FloatField(null=True,blank=True,default=0)
    kg1=models.FloatField(null=True,blank=True,default=0)
    kg1_5=models.FloatField(null=True,blank=True,default=0)
    kg2=models.FloatField(null=True,blank=True,default=0)
    kg2_5=models.FloatField(null=True,blank=True,default=0)
    kg3=models.FloatField(null=True,blank=True,default=0)
    kg3_5=models.FloatField(null=True,blank=True,default=0)
    kg4=models.FloatField(null=True,blank=True,default=0)
    kg4_5=models.FloatField(null=True,blank=True,default=0)
    kg5=models.FloatField(null=True,blank=True,default=0)
    kg5_5=models.FloatField(null=True,blank=True,default=0)

    kg6=models.FloatField(null=True,blank=True,default=0)
    kg6_5=models.FloatField(null=True,blank=True,default=0)
    kg7=models.FloatField(null=True,blank=True,default=0)
    kg7_5=models.FloatField(null=True,blank=True,default=0)
    kg8=models.FloatField(null=True,blank=True,default=0)
    kg8_5=models.FloatField(null=True,blank=True,default=0)
    kg9=models.FloatField(null=True,blank=True,default=0)
    kg9_5=models.FloatField(null=True,blank=True,default=0)
    kg10=models.FloatField(null=True,blank=True,default=0)
    kg11=models.FloatField(null=True,blank=True,default=0)
    kg12=models.FloatField(null=True,blank=True,default=0)
    kg13=models.FloatField(null=True,blank=True,default=0)
    kg14=models.FloatField(null=True,blank=True,default=0)
    kg15=models.FloatField(null=True,blank=True,default=0)
    kg16=models.FloatField(null=True,blank=True,default=0)
    kg17=models.FloatField(null=True,blank=True,default=0)
    kg18=models.FloatField(null=True,blank=True,default=0)
    kg19=models.FloatField(null=True,blank=True,default=0)
    kg20=models.FloatField(null=True,blank=True,default=0)
    kg_21_44=models.FloatField(null=True,blank=True,default=0)
    kg_45_70=models.FloatField(null=True,blank=True,default=0)
    kg_71_100=models.FloatField(null=True,blank=True,default=0)
    kg_101_299=models.FloatField(null=True,blank=True,default=0)
    kg_300_plus=models.FloatField(null=True,blank=True,default=0)








    def __str__(self):
        return self.company_name

class  save_data(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)

    phone=models.CharField(max_length=200,null=True,blank=True)
    email=models.CharField(max_length=200,null=True,blank=True)

    country=models.CharField(max_length=200,null=True,blank=True)
    length=models.CharField(max_length=200,null=True,blank=True)
    width=models.CharField(max_length=200,null=True,blank=True)
    height=models.CharField(max_length=200,null=True,blank=True)
    weight=models.CharField(max_length=200,null=True,blank=True)
    company_name=models.CharField(max_length=200,null=True,blank=True)
    company_price=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return  self.first_name


class Index(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    index=models.FloatField(null=True,default=1)


    def __str__(self):
        return f"{self.company.company_name}    ++ {self.country.country}  ++  {self.index}"


class AdditionalInformation(models.Model):
    channel_id = models.IntegerField(null=True, blank=True)
    kgforkub = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.kgforkub}"
