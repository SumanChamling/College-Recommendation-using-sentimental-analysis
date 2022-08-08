from django.http import request
from django.shortcuts import render, redirect
from django.views import View

from Recommendation.models import Review, collegereview
from Recommendation.models.m_oldschool import oldSchool
import re
pattern = re.compile(r'')

class PastSchool(View):
    def get(self, request):
        oldSchool.student_email = request.session['email']
        data = oldSchool.student_email
        table = oldSchool.objects.filter(student_email=data).exists()
        if table:
            pkid = request.session['email']
            data = oldSchool.objects.get(student_email=pkid)
            checkdata = Review.objects.filter(oldschool__startswith=data.pastSchool, schoollocation__startswith=data.address)
            context = {
                'Reviews': checkdata
            }
            return render(request, 'RecommendationModel.html', context)
        else:
            return render(request, 'oldschool.html')
    def post(self, request):
        postData = request.POST
        schoolnames = postData.get('sname')
        schoollocations = postData.get('slocation')
        request.session['School'] = schoolnames
        print(request.session['School'])
        request.session['Location'] = schoollocations
        student_email = request.session.get('email')
        schooldata = Review.objects.filter(oldschool=schoolnames, schoollocation=schoollocations).exists()
        if schooldata:
            print("fssdfsdf")
        else:
            return render(request, 'oldschool.html')
            # print("Sorrry, We cannot find your data")


        oldschool = oldSchool(pastSchool=schoolnames,
                              address=schoollocations,
                              student_email = student_email)

        error_message = None
        # validation


        value = {
            schoolnames:'schoolname',
            schoollocations:'schoollocation'
        }

        error_message = self.validationOldSchool(schoolnames,schoollocations)

        #saving
        if not error_message:
            oldschool.SaveOldSchool()
            return redirect('schoolname')

        else:
            data = {
                'error':error_message,
                'values':value
            }
            return render(request, 'oldschool.html', data)

    def validationOldSchool(self, schoolname,schoollocation):
        error_message = None
        if (not schoolname):
            error_message = "School name is required"
        elif (not schoollocation):
            error_message = "Schoollocation is required"
        elif re.search(r'[!@#$%&]', schoolname):
            error_message = "School name doesnot contain special character"
        elif re.search(r'[A-Z]', schoolname):
            error_message = "School name should be small letter"
        elif re.search(r'[!@#$%&]', schoollocation):
            error_message = "School location doesnot contain special character"
        elif re.search(r'[A-Z]', schoollocation):
            error_message= "School location should be in small letter"
        # elif schooldata:
        #     error_message="This email already provide schoolname and location "
        return error_message


