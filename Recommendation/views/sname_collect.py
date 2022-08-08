from django.shortcuts import render

from Recommendation.models import Review

def Sname_Collect(request):
    Sdata = Review.get_review_value()
    print(Sdata)
    List = []
    for sname in Sdata:
        Sname = sname.schoolname
        print("The school name is",Sname)
        List.append(Sname)
        print(List)

    length = len(List)
    print(length)
    count = 0
    element = 'dasd'

    for i in range(0, length):
        if element == List[i]:
            count += 1
    if count == 0:
        print(element, "Not found in given list")
    else:
        data = count/length
        print(data)

    return render(request, 'login.html')