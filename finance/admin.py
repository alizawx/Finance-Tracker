from django.contrib import admin
from .models import Account, Category, Transaction

# Register your models here.

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "account_name",
        "account_type",
        "currency",
        "opening_balance",
        "account_status",
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category_type",
        "user",
        "is_active",
    )

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "account",
        "category",
        "amount",
        "transaction_date",
    )