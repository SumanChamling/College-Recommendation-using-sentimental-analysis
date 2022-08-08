from django.views import View
import re
pattern = re.compile(r'')
from django.shortcuts import render, redirect

def Dashboard(request):
    return render(request, 'Dashboard.html')