from dataclasses import field
from .models import *
from rest_framework import serializers


class firstAPI(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'

class ProfileAPI(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'