from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'rmanage/index.html', {})

def register(request):
    return HttpResponse("Registration page.")

def advert(request, company):
    return render(request, 'rmanage/advert.html', {'company': company})

def apply_into(request, company):
    return HttpResponse("Form page of " + company )

def manage(request, company):
    return HttpResponse("Management page of " + company)

def see_notices(request, company):
    return HttpResponse("Notices page.")

def rdrive(request, company):
    return HttpResponse("Recruitment drive page.")

def create_rdrive(request, company):
    return HttpResponse("Recruitment drive form.")
