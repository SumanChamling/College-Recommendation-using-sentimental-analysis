from django.core.mail import send_mail
from django.shortcuts import render
from django.views import View
from django.contrib import messages


class PasswordReset(View):
    def get(self, request):
        return render(request,'password_reset.html')

    def post(self, request):
        email = request.POST.get('resetemail')
        request.session['sessionemail'] = email
        print(request.session['sessionemail'])
        send_mail(
            'New Password Message',
            'Hey!! you maya... http://127.0.0.1:8000/changepassword',
            'rajina_sunuwar99@gmail.com',
            [email],
            fail_silently=False,
        )
        messages.success(request, "Message send successfully")
        return render(request,'Home.html')
