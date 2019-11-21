from django.shortcuts import render, HttpResponse
from django.urls import reverse
from app01 import models


# Create your views here.
def index(request):
    # print('app01',reverse('app01:index'))
    # obj = models.UserInfo(username='alex', password='sb')
    # obj.save()
    # a,b = models.UserInfo.objects.update_or_create(
    #     username='111',
    #     defaults={
    #         'password':"2wwwwww"
    #     }
    # )
    # print(a,b)
    # ret = models.UserInfo.objects.all()
    # print(ret)
    # ret = models.UserInfo.objects.get(id=20)
    # print(ret)
    # print(ret.password)

    # print(reverse('app01:index'))


    # models.UserInfo.objects.create(username="111",password="2222")

    # models.UserInfo.objects.filter(id=1).update(password="dsb")

    # ret = models.UserInfo.objects.filter(id=1)
    # print(ret)
    # print(ret[0].username)
    # print(ret[0].password)
    # lst = []
    # for i in range(10):
    #     obj = models.UserInfo(username=str(i),password=str(i+1))
    #     obj.save()
        # lst.append(obj)
    # print(lst)
    # models.UserInfo.objects.bulk_create(lst)

    models.UserInfo.objects.filter(id=20).delete()




    return HttpResponse('app01index')
