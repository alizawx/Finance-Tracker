from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):

    class AccountType(models.TextChoices):
        BANK = "BK", "Bank"
        CASH = "CA", "Cash"
        WALLET = "WL", "Wallet"
        CREDIT_CARD = "CC", "Credit Card"

    class Currency(models.TextChoices):
        IRR = "IRR", "Iranian Rial"
        USD = "USD", "US Dollar"

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="accounts")

    account_name = models.CharField(max_length=50)

    account_type = models.CharField(
        max_length=2,
        choices=AccountType.choices
    )

    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
        default=Currency.IRR
    )

    opening_balance = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0
    )

    account_status = models.BooleanField(default=True)

    def __str__(self):
        return self.account_name