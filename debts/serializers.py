from rest_framework import serializers
from .models import Debt, ReturnDebt, CustomerUser


class CustomerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = ['id', 'username', 'store_name']


class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = '__all__'


class ReturnDebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnDebt
        fields = '__all__'
