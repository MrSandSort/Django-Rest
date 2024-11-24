from rest_framework import serializers
from .models import user, admin

class UserModelSerializers(serializers.ModelSerializer):
    class Meta:
        model= user
        fields='__all__'

class AdminModelSerializers(serializers.ModelSerializer):
    class Meta:
        model= admin
        fields='__all__'

class UserLoginSerializers(serializers.ModelSerializer):
    class Meta:
        models= user
        fields=['email', 'password']

class AdminLoginSerializers(serializers.ModelSerializer):
    class Meta:
        models= admin
        fields=['email','password']