
from rest_framework import serializers
from .models import Account
from django.contrib.auth.hashers import check_password


class AccountSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = Account
        fields = ("id","first_name","last_name", "username", "email",'password')
    
    def create(self, validated_data):
        account = Account.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        account.save()

        return account


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    class Meta:
        model = Account
        fields = ("id", "email","password",)
    
    # def is_valid(self, raise_exception, email, password):
    #     # email = self.validated_data['email']
    #     # password = self.validated_data['password']

    #     try:
    #         account = Account.objects.get(email=email)
    #     except:
    #         raise serializers.ValidationError('Account not exist')
        
    #     try:
    #         account_pass = Account.objects.get(email=email).password
    #         check_pass = check_password(password=password, encoded=account_pass)
    #     except:
    #         raise serializers.ValidationError('Account not exist')
    #     return account