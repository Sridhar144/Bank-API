"""banking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from .views import AccountView, WithdrawView, DepositView, TransactView, CheckView, HistoryView

urlpatterns = [
    path('accounts/', AccountView.as_view(), name="createacc"),
    path('accounts/<int:account>/withdraw/', WithdrawView.as_view(), name="withdraw"),
    path('accounts/<int:account>/deposit/', DepositView.as_view(), name="depo"),
    path('accounts/<int:account>/transact/', TransactView.as_view(), name="trans"),
    path('accounts/<int:account>/check/', CheckView.as_view(), name="check"),
    path('accounts/<int:account>/history/', HistoryView.as_view(), name="balance"),
]
