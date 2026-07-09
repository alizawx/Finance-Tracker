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

class Category(models.Model):

    class CategoryType(models.TextChoices):
        EXPENSE = 'EX','Expense'
        SPEND = 'SP','Spend'

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="categories")
    category_type = models.CharField(max_length=10,choices=CategoryType.choices)
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name

class Transaction(models.Model):

    account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="transactions")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="transactions")
    amount = models.DecimalField(max_digits=15,decimal_places=2)
    description = models.CharField(max_length=100, blank=True)
    transaction_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-transaction_date']

    def __str__(self):
        return f"{self.category.name} {self.amount}"




