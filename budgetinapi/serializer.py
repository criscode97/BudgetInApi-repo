from dataclasses import fields
from django.contrib.auth.models import User
from django.db.models import Sum
from rest_framework import serializers
from .models import Expenses, Income
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
    

class UserBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fiels = ['username', 'id']

class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = '__all__'

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['title', 'total', 'id']


