from django.shortcuts import render

from Recommendation.models import Review


def Rate_collect(request):

    reviewdata = Review.get_review_value()
    listt = []
    for data in reviewdata:
        rating_count = data.rating
        listt.append(rating_count)
    length = len(listt)
    print(length)
    count = 0
    element = 5

    for i in range(0, length):
        if element == listt[i]:
            count+= 1
    if count==0:
        print(element,"Not found in given list")
    else:
        data = count/length
        print(data)

    return render(request,'college.html')

