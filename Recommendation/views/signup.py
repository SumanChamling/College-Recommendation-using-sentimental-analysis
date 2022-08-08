import re
import uuid

from django.views import View
from django.contrib.auth.hashers import make_password

from Recommendation.models import Models_Profile
from Recommendation.views.utils import send_email_token

pattern = re.compile(r'')
from django.shortcuts import render, redirect
from Recommendation.models.register import Register
from django.contrib import messages

class Signup(View):
    def get(self,request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        name = postData.get('name')
        email = postData.get('email')
        password = postData.get('password')
        address = postData.get('address')
        phone = postData.get('phone')

        p_obj = Models_Profile.objects.create(
            email_token=str(uuid.uuid4())
        )
        save_Profile = Models_Profile(
            email=email,
            email_token=p_obj.email_token
        )
        save_Profile.saveProfile()
        send_email_token(email, p_obj.email_token)

        register = Register(name=name,
                            email=email,
                            password=password,
                            address=address,
                            phone=phone)

        error_message = None
        # Validation
        value = {
            'name': name,
            'email': email,
            'address': address,
            'phone': phone
        }
        error_message = self.ValidateRegister(name, password, phone, register)
        # Saving
        if not error_message:
            register.password = make_password(register.password)
            register.registerData()
            # Register.objects.create(
            #     register = User,
            # )
            messages.success(request, "Successfully send token to your gmail")
            return redirect('login')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def ValidateRegister(self, name, password, phone, register):
        error_message = None
        if (not name):
            error_message = "Name is required!!"
        elif len(name) < 5:
            error_message = "First name must be 5 character"
        elif re.search(r'[!@#$%&]', name):
            error_message = "Name doesnot contain special character"
        elif not password:
            error_message = "Password is required"
        elif re.search(r'[!@#$%&]', password) is None:
            error_message = "Password must contains atleast one special symbol"
        elif re.search(r'\d', password) is None:
            error_message = "password must contain atleast one digits"
        elif re.search('[A-Z]', password) is None:
            error_message = "Password must contain one capital letters"
        elif len(password) < 6:
            error_message = "Password must be 6 characters"
        elif not phone:
            error_message = "Phone is required"
        elif len(phone) < 10:
            error_message = "Phone number should be 10 characters"
        elif register.isExist:
            error_message = "Email is Already Used"
        return error_message