from django.shortcuts import render
from django.views import View

from Recommendation.models import oldSchool, Review


class CheckStudents(View):
    def get(self, request):
        oldSchool.student_email = request.session['email']
        data = oldSchool.student_email
        table = oldSchool.objects.filter(student_email=data).exists()
        if table:
            pkid = request.session['email']
            data = oldSchool.objects.get(student_email=pkid)
            checkdata = Review.objects.filter(oldschool__startswith=data.pastSchool,
                                              schoollocation__startswith=data.address)
            context = {
                'Reviews': checkdata
            }
            return render(request, 'RecommendationModel.html', context)
        else:
            return render(request, 'oldschool.html')