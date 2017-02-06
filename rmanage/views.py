from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'rmanage/index.html', {})

def register(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data
            f.save()
            return render(request, 'rmanage/thanks.html', {})
    else:
        form = CompanyForm()

    return render(request, 'rmanage/register.html', {'form': form})

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

def rdrive_create(request, company):
    return HttpResponse("Recruitment drive form.")

def panel(request, company):
    return HttpResponse("View Panels")

def create_panel(request, company):
    return HttpResponse("Panel create form.")
