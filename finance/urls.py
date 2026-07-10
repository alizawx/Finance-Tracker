from django.urls import path
from .views import DashboardView,TransactionListView

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("transactions/",TransactionListView.as_view(),name="Transaction")
]