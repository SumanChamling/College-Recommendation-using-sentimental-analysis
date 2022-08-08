from django.core.mail import send_mail
import re
from Recommendation.models.AddCollege import AddColleges
from .review import Review
from Recommendation.models.m_oldschool import oldSchool
from Recommendation.models.register import Register

from django.views import View

from ..models import register, Models_Profile

pattern = re.compile(r'')
from django.shortcuts import render, redirect


def Search(request):
    query = request.GET['Search']
    all_school = AddColleges.objects.filter(name__icontains = query)
    context = {
        'addcollege': all_school,
    }
    return render(request, 'college.html', context)

def College(request):


    # send_mail(
    #     'fuckin program',
    #     'Hey!! you fuck... http://127.0.0.1:8000/college',
    #     'rajina_sunuwar99@gmail.com',
    #     ['rawvideos87@gmail.com'],
    #     fail_silently=False,
    # )
    # session = request.session['registers_id']
    # if register.test():
    #     print("We got it")

    #It pick out all the data smiller to sc from database
    # sname = request.session['school']
    # slocation = request.session['location']
    # dataa = Review.objects.filter(oldschool__startswith = sname, schoollocation__startswith = slocation)
    # # print(dataa)
    # for da in dataa:
    #     print(da.collegeReview)

    # dat = Register.objects.all()
    # for d in dat:
    # print("dasdasdas",Register.school_id.email)


    # int = Review.get_school_name()
    # print("SFsadf", int)
    # int = request.session['email']
    # print(int)
    #
    #
    # # data = m_oldschool.email_check
    #
    # def get_review_from_data(int):
    #     try:
    #         return Review.objects.get(registered_email=int)
    #     except:
    #         return False
    #
    # data = Review.get_review_from_data(int)
    # print(data.rating)

    # subjectData = request.GET.get('oldschool')
    # print("Result",subjectData)
    # dataa = Review.get_review_value()
    #
    # for data in
    global data, n
    review0 = Review.objects.all()
    for review in review0:
        data = review.pk
        # print(data)

    review2 = Review.objects.all()
    for reviews in review2:
        print(reviews.oldschool)
    #     # data1 = reviews.schoolname
    #     # if data1 == 'fasdf':
    #     #     print("Fuck")
            # review3 = Review.objects.all()
            # for reviewss in review3:
            #     if reviewss.rating>2:





            # review1 = Review.objects.get(pk=data)
            # print(review1.rating)
            # if review1.rating > 1:
            #     print("The school name is")
                # for data1 in review1.schoolname:
        #         #     print(data1)
        # else:
        #     print("do not contain value")


    reviewdata = Review.get_review_value()
    listt = []

    for data in reviewdata:
        rating_count = data.collegeName
        listt.append(rating_count)
    length = len(listt)
    print("The list of length is",length)
    count = 0
    element = 'new millinium college'

    for i in range(0, length):
        if element == listt[i]:
            acount = count+1
            print(acount)

    if count == 0:
        print(element, "Not found in given list")
    else:
        data = count / length
        print(data)

    colleges = AddColleges.get_all_college()
    # dss = Register.school_id()
    # print(dss.email)
    # ds = Register.objects.all()
    # for d in ds:
    #     print(d.school_id)

    # data = Review.objects.filter(oldschool = 'dasd')
    # for s in data:
    #     print(s.collegeReview)



    # data = Review.objects.filter(id__in=[17,21,23,24,25,26])
    # for s in data:
    #     print("fsfsdfsdf",s.oldschool)
    # for e in Review.objects.filter(collegeName__startswith = 'brilliant multiple campus' ):
    #     ee = e.collegeReview
    # request.session['description'] = colleges.description
    # data = AddColleges.get_session_college()
    # request.session['description'] = data

    context = {
    'addcollege': colleges,
    # 'reviewdata': data,
    'reviews':reviewdata
    }
    return render(request, 'college.html', context)
