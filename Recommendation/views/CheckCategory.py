from django.shortcuts import render

from Recommendation.models import oldSchool


def CheckSorC(request):
    return render(request, 'CheckSchoolCategory.html')
