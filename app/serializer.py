from rest_framework import serializers
from .models import OcservUser

class OcServUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = OcservUser
        fields = "__all__"
