from rest_framework import generics, serializers
from .models import Account, Transaction
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields=['account', 'owner', 'balance']
    


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields=['id','account','transaction_choice','amount','description','timestamp']