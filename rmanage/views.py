from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from rmanage.models import *
import datetime
from .forms import *
from .models import *

def index(request):
    return render(request, 'rmanage/index.html', {})

def register(request):
    if request.method == 'POST':
         form = CompanyForm(request.POST)
         if form.is_valid():
             form.cleaned_data
             instance = form.save()
             return render(request, 'rmanage/thanks.html', {})
    else:
        form = CompanyForm()
 
    return render(request, 'rmanage/register.html', {'form': form})    

def advert(request, company):
    if request.user.is_authenticated:
        is_collab = 1
    else:
        is_collab = 0
    return render(request, 'rmanage/advert.html', {
                    'company': company,
                    'is_collab': is_collab
                    }
                )

def apply_into(request, company):
    return HttpResponse("Form page of " + company )

def manage(request, company):
    now = datetime.datetime.now() 
    ongoingDrives = RecruitmentDrive.objects.filter(end_date__gte=now).order_by('end_date')
    previousDrives = RecruitmentDrive.objects.filter(end_date__lte=now).order_by('end_date')  
    return render(request, 'rmanage/manage.html',{
                     'ongoingDrives': ongoingDrives, 
                     'previousDrives': previousDrives,
                     'company': company
                     }
                 )

def see_notices(request, company):
    return HttpResponse("Notices page.")

def rdrive(request, company, r_id):
    return HttpResponse("Recruitment drive page.")

def rdrive_create(request, company):
    if request.method == 'POST':
         form = RecruitmentDriveForm(request.POST)
         company = company.lower()
         company = Company.objects.get(name=company);          
         date_created = datetime.date.today()
         if form.is_valid():
             form.cleaned_data
             instance = form.save(commit=False)
             instance.company = company
             instance.date_created = date_created
             instance.save()
             return render(request, 'rmanage/rdrive_added.html', {})
      
    else:
        form = RecruitmentDriveForm()
 
    return render(request, 'rmanage/rdrive_create.html', {'form': form, 'company': company})    



def rdrive_start(request, company):
    return HttpResponse("Start a new recruitment drive")

def panel(request, company):
    return HttpResponse("View Panel")

def create_panel(request, company):
    return HttpResponse("Create a panel")

def add_members(request, company):
    return HttpResponse("Add collaborators")

def add_notice(request, company):
    return HttpResponse("Add a notice")

def view_candidates(request, company):
    return HttpResponse("View Candidate")

def rdrive_edit(request,company):
    return HttpResponse("Edit Recruitment Drive")

def collab_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                company = Collaborator.objects.get(hr=user).company.name
                manage_url = '/rmanage/company/' + company + '/manage/'
                return HttpResponseRedirect(manage_url)
        else:
            return render(request, 'rmanage/login.html', {
                                'error_message': 'Invalid Credentials'
                                    })
    else:
        return render(request, 'rmanage/login.html', {})

@login_required
def collab_logout(request):
    logout(request)
    return HttpResponseRedirect('/rmanage/')
