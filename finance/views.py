from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Account,Category,Transaction
from django.db.models import Sum
from django.views.generic import ListView
from django.core.paginator import Paginator
# Create your views here.

class DashboardView(TemplateView):
    template_name = "finance/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["account_count"] = Account.objects.count()
        context["category_count"] = Category.objects.count()
        context["transactions_count"] = Transaction.objects.count()

        income = Transaction.objects.filter(category__category_type=Category.CategoryType.INCOME).aggregate(total=Sum('amount'))
        expense = Transaction.objects.filter(category__category_type=Category.CategoryType.EXPENSE).aggregate(total=Sum('amount'))

        context["total_income"] = income['total'] or 0
        context["total_expense"] = expense['total'] or 0
        context["balance"] = context["total_income"] - context["total_expense"]
        return context

class TransactionListView(ListView):
    model = Transaction
    template_name = "finance/transaction_list.html"
    context_object_name = "transactions"
    paginate_by = 2
