from django.shortcuts import render
from django.views import View

from Recommendation.models import Review


def schoolName(request):
    snames = request.session['School']
    slocations = request.session['Location']
    schooldata = Review.objects.filter(oldschool__startswith = snames, schoollocation__startswith = slocations)
    List = []
    for review in schooldata:
        d = review.collegeReview
        List.append(d)
    context = {
        'Reviews':schooldata
    }
    return render(request, 'RecommendationModel.html', context)