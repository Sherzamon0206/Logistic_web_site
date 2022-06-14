from django.shortcuts import render
from .models import *
import json
from django.http import JsonResponse

import requests



def CalculatorPageView(request):
    DATA=Country.objects.all()

    return render(request=request,template_name='index.html', context={"country":DATA})
def Calculator(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        weight=data['weight']
        print(weight)
        return JsonResponse({'data': 'ok'})

    return render(request=request,template_name='index.html')

def CompanySendFunc(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        kg=int(data['weight'])
        comp=Company.objects.all()

        country=data['country']


        if kg==15:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=i.kg15*koeffisent




                a ={
                    'logo': i.company_logo,
                    'type': i.company_type,
                    'name':i.company_name,

                    'time':i.days,
                    'price':narx}
                data.append(a)
        if kg==0.5:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=i.kg05*koeffisent
                a ={'name':i.company_name,
                    'time':i.days,'price':int(narx),
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    }
                data.append(a)
        if kg==1:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=i.kg1*koeffisent

                a ={'name':i.company_name,'time':i.days,'price':int(narx),
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    }
                data.append(a)

        if kg==1.5:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=i.kg1_5*koeffisent

                a ={'name':i.company_name,'time':i.days,'price':int(narx),
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    }
                data.append(a)
        if kg==2:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg2
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if kg==2_5:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg2_5
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if kg==3:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg3
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if kg==3_5:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg3_5
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if kg==4:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg4
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if kg==4_5:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg4_5
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if kg==5:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg5
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if kg==5_5:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg5_5
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if kg==6:
            data=[]
            for i in comp:

                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg6
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if kg==6_5:
            data=[]
            for i in comp:

                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg6_5
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if kg==7:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg7
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if kg==7_5:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg7_5
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if kg==8:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=i.kg8*koeffisent
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if kg==8_5:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=i.kg8_5*koeffisent
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if kg==9:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg9
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if kg==9_5:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg9_5
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if kg==10:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg10
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if kg==11:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg11
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if kg==12:
            data=[]

            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg12
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if kg==13:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg13
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if kg==14:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg14
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if kg==15:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg15
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if kg==16:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg16
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if kg==17:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg17
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if kg==18:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg18
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if kg==19:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg19
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if kg==20:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg20
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if  20<kg<45:
            data=[]

            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx =i.kg_21_44 * kg*koeffisent
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if  44<kg<71:
            data=[]

            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx =i.kg_21_44 * kg*koeffisent
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if  70<kg<101:
            data=[]

            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx =i.kg_21_44 * kg*koeffisent
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if  100<kg<300:
            data=[]

            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx =i.kg_21_44 * kg*koeffisent
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        if  299<kg:
            data=[]

            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx =i.kg_21_44 * kg*koeffisent
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':int(narx)}
                data.append(a)
        return JsonResponse({'data': data})

    return render(request=request,template_name='index.html')
def Saqlash(request):
    if request.method == 'POST':
        addition = AdditionalInformation.objects.first()
        data = json.loads(request.body)
        name = data['name']

        phone = data['phone']
        email = data['email']

        country = data['country']
        length = data['length']
        width = data['width']
        height = data['height']
        weight = data['weight']
        company_name = data['company_name']
        company_price = data['company_price']
        text=f"name:{name}\nphone:{phone}\nemail: {email}\ncountry:{country}\nlength:{length} sm\nwidth:{width} sm\nheight:{height} sm\nweight:{weight} kg\n{company_name}\n{company_price}"
        try:
            requests.post(
                f'https://api.telegram.org/bot5191254844:AAHjg0ocEF6eS9p8H_xL1cCfrEo6oKYX8HI/sendMessage?chat_id=-100{addition.channel_id}&text={text}')
        except Exception as e:
            pass





        save_data.objects.create(name=data['name'],phone=data['phone'],
                                 email=data['email'],country=data['country'],
                                 length=data['length'],width=data['width'],height=data['height'],weight=data['weight'],company_name=data['company_name'],company_price=data['company_price'])




        return JsonResponse({'data': 'ok'})