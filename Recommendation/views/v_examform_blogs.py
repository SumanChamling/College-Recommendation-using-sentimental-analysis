
from django.shortcuts import render

from Recommendation.models import Review, Faculty


def ExamForm(request):
    global reviews
    Review.registered = request.session['email']
    data = Review.registered
    print("The email id",data)
    table = Review.objects.filter(registered_email=data).exists()
    if table:
        return render(request,'ExamForm.html')
    else:
        results = Faculty.objects.all()
        return render(request,'review.html',{'showFaculty': results})


def Blogs(request):
    return render(request, 'Blogs.html')