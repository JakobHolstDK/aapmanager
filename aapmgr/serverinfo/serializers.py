from rest_framework import serializers
from .models import Asset, Server, appid

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = '__all__'

class AppidSerializer(serializers.ModelSerializer):
    class Meta:
        model = appid
        fields = '__all__'
