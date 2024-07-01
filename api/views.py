from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Account, Transaction
# from django.views.generic import CreateView
from .serializers import AccountSerializer, TransactionSerializer
from decimal import Decimal
# Create your views here.
class AccountView(generics.CreateAPIView):
    account=Account.objects.all()
    serializer_class=AccountSerializer

class WithdrawView(APIView):
    def post(self, request, account):
        try:
            account=Account.objects.get(account=account)
            data=request.data
            # print(data)
            # print(type(data))
            amount=Decimal(data['amount'])
            if amount<account.balance:
                account.balance-=amount
                account.save()
                Transaction.objects.create(account=account, amount=amount, transaction_choice='Withdraw', description="money successfully withdrawn")
                return Response({'message':"money withdrawn successfully"}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'error':"insufficient money"}, status=status.HTTP_400_BAD_REQUEST)
        except Account.DoesNotExist:
            return Response({'error':"account not found"}, status=status.HTTP_404_NOT_FOUND)
        

        

class DepositView(APIView):
    def post(self, request, account):
        try:
            account=Account.objects.get(account=account)
            amount=Decimal(request.data['amount'])
            account.balance+=amount
            account.save()
            Transaction.objects.create(account=account, amount=amount, transaction_choice='Deposit', description="money successfully deposited")
            return Response({'message':"money deposited successfully"}, status=status.HTTP_202_ACCEPTED)
        except Account.DoesNotExist:
            return Response({'error':"account not found"}, status=status.HTTP_404_NOT_FOUND)
        



class TransactView(APIView):
    def post(self, request, account):
        try:
            data=request.data
            print(data)
            print(type(data))
            # from_account=data['from_account']
            to_account=data['to_account']
            
            account_from=Account.objects.get(account=account)
            account_to=Account.objects.get(account=to_account)
            amount=Decimal(data['amount'])
            print(amount)
            print(account_from.balance)
            if amount<account_from.balance:
                account_from.balance-=amount
                account_to.balance+=amount

                account_from.save()
                account_to.save()
                Transaction.objects.create(account=account_from, amount=amount, transaction_choice='Transaction_fr', description="money successfully withdrawn using transaction")
                Transaction.objects.create(account=account_to, amount=amount, transaction_choice='Transaction_to', description="money successfully deposited using transaction")
                return Response({'message':"money trasaciton successful"}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'error':"insufficient money"}, status=status.HTTP_400_BAD_REQUEST)
        except Account.DoesNotExist:
            return Response({'error':"account not found"}, status=status.HTTP_404_NOT_FOUND)


class CheckView(APIView):
    # def get(self, request, account):
    #     try:
    #         account = Account.objects.get(account=account)
    #         serializer = AccountSerializer(account)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     except Account.DoesNotExist:
    #         return Response({'error': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)
    def get(self, request, account):
        try:
            account=Account.objects.get(account=account)
            serializer=AccountSerializer(account)
            return Response(serializer.data , status=status.HTTP_202_ACCEPTED)
            
        except:
            return Response({'error': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)
            

class HistoryView(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        account_number = self.kwargs['account']
        return Transaction.objects.filter(account__account=account_number)