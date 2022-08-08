
import re
import uuid

import sweetify
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.hashers import check_password
from django.contrib import messages

from Recommendation.models import m_oldschool, Models_Profile
from Recommendation.views.utils import send_email_token

pattern = re.compile(r'')
from django.shortcuts import render, redirect
from Recommendation.models.m_oldschool import oldSchool
# from Recommendation.models.profiles import Profile
from Recommendation.models.register import Register


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        register = Register.get_student_by_email(email)
        # valid = Models_Profile.objects.get(pk=3)
        # register = Register.get_email_verified(email)
        # registerCheck = Register.check_student_by_email(email)
        error_message = None
        try:
            if register:
                flag = check_password(password, register.password)
                if flag:
                    request.session['registers_id'] = register.id
                    request.session['name'] = register.name
                    request.session['email'] = register.email
                    Display_id = request.session.get('register_id')
                    Display_name = request.session.get('name')
                    context = {
                        'data_id': Display_id,
                        'data_name': Display_name
                    }
                # if m_oldschool.email_check:
                #     print("I got it")
                #     return redirect('DashboardHome')
                # else:
                #     print("I didnt got it")
                    return render(request, 'DashboardHome.html', context)
                else:
                    error_message = "Email or password invalid"
                    return render(request, 'login.html', {'error': error_message})
        except Exception:
            return HttpResponse("This email doesnot exist")

def logout(request):
    request.session.clear()
    return redirect('login')

def verify(request, token):
    try:
        obj = Models_Profile.objects.get(email_token =  token)
        obj.is_verified = True
        obj.save()
        messages.success(request, "Your Account is verified")
        return render(request, 'login.html')
    except Exception as e:
        messages.success(request, "Invalid token")
        return render(request, 'signup.html')