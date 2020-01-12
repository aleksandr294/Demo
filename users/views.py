from django.shortcuts import render
from rest_framework.generics import *
from .models import *
from .serializer import *
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.decorators import api_view

def makeListUsers():
    count = User.objects.all().count()
    total_list = []
    total_object = []
    for index in range(1, count):
        total_list.append(
            [
                index,
                User.objects.get(user_id = index).first_name,
                User.objects.get(user_id = index).last_name,
                User.objects.get(user_id = index).email,
                User.objects.get(user_id = index).gender,
                User.objects.get(user_id = index).ip_address,
                Statistic.objects.filter(user = index).aggregate(Sum('page_views')),
                Statistic.objects.filter(user = index).aggregate(Sum('clicks'))
            ]
        )
    for item in total_list:
        total_object.append(Total(item[0], item[1], item[2], item[3], item[4], item[5], item[6]['page_views__sum'], item[7]['clicks__sum']))         
    return total_object



@api_view(['GET'])
def userStatListView(request, user):
    if request.method == 'GET':
        if Statistic.objects.filter(user = user).exists():
            userStatList = Statistic.objects.filter(user = user).order_by('date')
            serializer = StatisticSerializer(userStatList, many = True)
            return Response(serializer.data)
        else:
            return Response('Такого пользователя не существует', status=404)

@api_view(['GET'])
def userStatListDateView(request, user, firstData = None, lastData = None):
    if request.method == 'GET':
        print(firstData)
        if Statistic.objects.filter(user = user).exists():
            userStatList = Statistic.objects.filter(user = user, date__gte = firstData, date__lte = lastData)
            serializer = StatisticSerializer(userStatList, many = True)
            return Response(serializer.data)
        else:
            return Response('Такого пользователя не существует', status=404)

class UsersListView(ListAPIView):
    serializer_class = TotalSerializer
    queryset = makeListUsers()

class UserStatisticListView(ListAPIView):
    serializer_class = StatisticSerializer
    queryset = Statistic.objects.all()