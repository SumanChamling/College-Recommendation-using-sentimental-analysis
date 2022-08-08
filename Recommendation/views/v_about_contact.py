from django.shortcuts import render


def About(request):
    return render(request, 'aboutus.html')

def Contact(request):
    return render(request, 'contact.html')