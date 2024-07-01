from django.db import models

# Create your models here.
class Account(models.Model):
    account=models.AutoField(primary_key=True)
    owner=models.CharField(max_length=80)
    balance=models.DecimalField(decimal_places=2, default=0.00, max_digits=10)

class Transaction(models.Model):
    Choice = (
        ('deposit', 'Deposit'),
        ('withdraw', 'Withdraw'),
        ('transactionfr', 'Transaction_fr'),
        ('transactionto', 'Transaction_to'),
    )
    account=models.ForeignKey(Account , related_name='transactions' , on_delete=models.CASCADE)
    transaction_choice=models.CharField(choices=Choice, max_length=15)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    description=models.CharField(max_length=100, blank=True, null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.transaction_choice}-{self.amount}'
    

    # create account
    # transact here to there
    # deposit
    # withdraw
    # check balanace
    # transaction history