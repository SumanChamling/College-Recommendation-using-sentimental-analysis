from urllib import request

import forloop as forloop
from django.shortcuts import render, redirect
from django.views import View

from Recommendation.models import Review, Faculty, oldSchool


class Recommend(View):
    def get(self, request):
        global reviews
        Review.registered = request.session['email']
        data = Review.registered
        print("Registered Email is",Review.registered)
        review2 = Review.objects.all()
        for reviews in review2:
            data1 = reviews.registered_email
            print(data1)
            table = Review.objects.filter(registered_email = data).exists()
            if table:
                #This is important code that we can choose any of the data as per the email and oldschool
                # pkid = request.session['email']
                # data = Review.objects.get(registered_email = pkid )
                # print(data.oldschool)
                # schooldata = Review.objects.filter(oldschool__startswith=data.oldschool, schoollocation__startswith=data.schoollocation)
                context = {
                    # 'Reviews': schooldata
                }
                return render(request,'sorrypages.html')
            else:
                results = Faculty.objects.all()
                return render(request, 'review.html', {'showFaculty': results})


    # else:
    #     def get(self, request):
    #         results = Faculty.objects.all()
    #         return render(request, 'review.html', {'showFaculty': results})


