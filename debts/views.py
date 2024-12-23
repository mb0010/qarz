from rest_framework import viewsets
from .models import Debt, ReturnDebt, CustomerUser
from .serializers import DebtSerializer, ReturnDebtSerializer, CustomerUserSerializer


class CustomerUserViewSet(viewsets.ModelViewSet):
    queryset = CustomerUser.objects.all()
    serializer_class = CustomerUserSerializer


class DebtViewSet(viewsets.ModelViewSet):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer


class ReturnDebtViewSet(viewsets.ModelViewSet):
    queryset = ReturnDebt.objects.all()
    serializer_class = ReturnDebtSerializer
