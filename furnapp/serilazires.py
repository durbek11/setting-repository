from dataclasses import field
from .models import *
from rest_framework import serilaizers


class firstAPI(serializers.ModelSerializer):
    class Meta:
        model = firstAPI
        fields = '__all__'