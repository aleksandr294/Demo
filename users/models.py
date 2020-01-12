from django.db import models

class User(models.Model):
    user_id = models.IntegerField(verbose_name ='Индекс юзера', db_index = True)
    first_name = models.CharField(verbose_name ='Имя юзера', max_length = 64)
    last_name = models.CharField(verbose_name ='Фамилия юзера', max_length = 64)
    email = models.EmailField(verbose_name ='Фамилия юзера')
    gender = models.CharField(verbose_name ='Пол юзера', max_length = 10)
    ip_address = models.GenericIPAddressField(verbose_name ='Ip адресс юзера')

class Statistic(models.Model):
    user = models.ForeignKey('User', on_delete = models.CASCADE)
    date = models.DateField(verbose_name ='Дата')
    page_views = models.IntegerField(verbose_name ='Просмотр страницы')
    clicks = models.IntegerField(verbose_name ='Клики')