from rest_framework import serializers
from .models import User, Statistic

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id','first_name', 'last_name', 'email', 'gender', 'ip_address')

class StatisticSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Statistic
        fields = ('user', 'date', 'page_views', 'clicks')

class Total(object):
    def __init__(self, user_id, first_name, last_name, email, gender, ip_address, total_clicks, total_page_views):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.ip_address = ip_address
        self.total_clicks = total_clicks
        self.total_page_views = total_page_views

class TotalSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    first_name = serializers.CharField(max_length = 64)
    last_name = serializers.CharField(max_length = 64)
    email = serializers.EmailField()
    gender = serializers.CharField(max_length = 10)
    ip_address = serializers.IPAddressField()
    total_clicks = serializers.IntegerField()
    total_page_views = serializers.IntegerField()