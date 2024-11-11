from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import filters

from .models import Account
from .forms import AccountForm
from .serializers import AccountSerializer


def AccountList(request):
    accounts = Account.objects.all()
    return render(request, 'account/account_list.html', {'accounts': accounts})


def AccountCreate(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '계정이 성공적으로 생성되었습니다.')
            return redirect('account:account_list')
    else:
        form = AccountForm()
    return render(request, 'account/account_form.html', {'form': form})


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    pagination_class = PageNumberPagination