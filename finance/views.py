from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Account,Category,Transaction
# Create your views here.

class DashboardView(TemplateView):
    template_name = "finance/dashboard.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["account_count"] = Account.objects.count()
        context["category_count"] = Category.objects.count()
        context["transactions_count"] = Transaction.objects.count()

        return context