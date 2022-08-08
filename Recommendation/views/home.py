import re

from django.http import request
from django.views import View
from pyexpat.errors import messages

pattern = re.compile(r'')
from django.shortcuts import render, redirect


def homePages(request):
    int = request.session.get('registers_id')
    print(int)
    return render(request, 'Home.html')





