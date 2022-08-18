from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user



class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

    def validate(self, data):
        if data['account_name']:
            for n in data['account_name']:
                if n.isdigit():
                    raise serializers.ValidationError({'error' : 'name cannot contain number'})
        return data


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'