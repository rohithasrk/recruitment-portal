from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'rmanage/index.html', {})

def register(request):
    return HttpResponse("Registration page.")

def advert(request, company):
    return HttpResponse("Advert page of " + company)

def apply_into(request, company):
    return HttpResponse("Form page of " + company )

def manage(request, company):
    return HttpResponse("Mangement page of " + company)
