from rest_framework import serializers
from .models import application

# Create your serializers here.where all tables are joined
class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = application
        fields = '__all__'