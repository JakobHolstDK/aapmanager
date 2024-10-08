from rest_framework import serializers
from .models import server, zone, region, appid, environment, serverrole,  organization, project, country

# Create your serializers here.where all tables are joined
class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = organization
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields = '__all__'

class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = server
        fields = '__all__'

class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = zone
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = region
        fields = '__all__'

class AppidSerializer(serializers.ModelSerializer):
    class Meta:
        model = appid
        fields = '__all__'

class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = environment
        fields = '__all__'

class ServerroleSerializer(serializers.ModelSerializer):
    class Meta:
        model = serverrole
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = country
        fields = '__all__'



