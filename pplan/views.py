from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import filters

from .models import Pplan
from .forms import PplanForm
from .serializers import PplanSerializer

def PplanList(request):
    pplans = Pplan.objects.all()
    return render(request, 'pplan/pplan_list.html', {'pplans': pplans})

def PplanCreate(request):
    if request.method == 'POST':
        form = PplanForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '가격 정보가 성공적으로 생성되었습니다.')
            return redirect('pplan:pplan_list')
    else:
        form = PplanForm()
    return render(request, 'pplan/pplan_form.html', {'form': form})

def PplanCreate(request):
    if request.method == 'POST':
        form = PplanForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '가격 정보가 성공적으로 생성되었습니다.')
            return redirect('pplan:pplan_list')
    else:
        form = PplanForm()
    return render(request, 'pplan/pplan_form.html', {'form': form})

class PplanViewSet(viewsets.ModelViewSet):
    queryset = Pplan.objects.all()
    serializer_class = PplanSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    pagination_class = PageNumberPagination
