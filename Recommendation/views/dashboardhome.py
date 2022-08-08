from django.views import View
import re

pattern = re.compile(r'')
from django.shortcuts import render, redirect


def DashboardHome(request):
    return render(request, 'DashboardHome.html')
