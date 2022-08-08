from django.shortcuts import render, redirect
from django.views import View
import re
pattern = re.compile(r'')
from Recommendation.models import Register
from django.contrib.auth.hashers import make_password


class ChangePassword(View):
    def get(self, request):
        return render(request,'passwordchanges.html')
    def post(self, request):
        password = request.POST.get('passwords')
        confirmpassword = request.POST.get('cpasswords')
        cpass = make_password(confirmpassword)
        d = request.session['sessionemail']
        e = Register.objects.get(email=d)
        f = e.id
        error_message = self.ValidatePassword(password, confirmpassword)
        if not error_message:
            Register.objects.filter(pk=f).update(password=cpass)
            return redirect('homepage')
        else:
            data = {
                'error':error_message,
            }
            return render(request, 'passwordchanges.html', data)

    def ValidatePassword(self,password, confirmpassword ):
        error_message = None
        if len(password) < 6:
            error_message = "First name must be 5 character"
        elif len(confirmpassword) < 6:
            error_message = "Confiram password must be 6 characters"
        elif(password != confirmpassword):
            error_message = "Password and confirm password doesnot match"
        elif re.search(r'[!@#$%&]', password) is None:
            error_message = "Password must contains atleast one special symbol"
        elif re.search(r'\d', password) is None:
            error_message = "password must contain atleast one digits"
        elif re.search('[A-Z]', password) is None:
            error_message = "Password must contain one capital letters"
        return error_message





