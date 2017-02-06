from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

import datetime

from .models import *
from .forms import *


def index(request):
    return render(request, 'rmanage/index.html', {})


def register(request):
    if request.method == 'POST':
         form = CompanyForm(request.POST)
         if form.is_valid():
             company = form.save(commit=False)
             company.save()
             admin = User(username=company.email, password=company.password)
             admin.save()
             admin = CompanyAdmin(admin=admin, company=company)
             admin.save()
             return render(request, 'rmanage/thanks.html', {})
    else:
        form = CompanyForm()
    
    return render(request, 'rmanage/register.html', {'form': form})


def advert(request, company):
    if company_exists(company):
        return render(request, 'rmanage/advert.html', {
                        'company': company,
                        }
                    )
    else:
        raise Http404()


def apply_into(request, company):
    if company_exists(company):
        return HttpResponse("Form page of " + company )
    else:
        raise Http404()


@login_required
def manage(request, company):
    if company_auth(request, company):
        now = datetime.datetime.now() 
        ongoingDrives = RecruitmentDrive.objects.filter(end_date__gte=now).order_by('end_date')
        previousDrives = RecruitmentDrive.objects.filter(end_date__lte=now).order_by('end_date')  
        
        return render(request, 'rmanage/manage.html',{
                         'ongoingDrives': ongoingDrives, 
                         'previousDrives': previousDrives,
                         'company': company
                         }
                     )
    else:
        raise Http404()


def see_notices(request, company):
    if company_exists(company):
        return HttpResponse("Notices page.")
    else:
        raise Http404()


@login_required
def rdrive(request, company, r_id):
    if company_auth(request, company):
        return HttpResponse("Recruitment drive page.")
    else:
        raise Http404()


@login_required
def create_rdrive(request, company):
    if is_admin(request, company):
        return HttpResponse("Recruitment drive form.")
    else:
        raise Http404()


@login_required
def rdrive_start(request, company):
    if is_admin(request, company):
        return HttpResponse("Start a new recruitment drive")
    else:
        raise Http404()


@login_required
def rdrive_create(request, company):
    if is_admin(request, company):
        return HttpResponse("Create a recuitment drive")
    else:
        raise Http404()


@login_required
def panel(request, company):
    if company_auth(request, company):
        return HttpResponse("View Panel")


@login_required
def create_panel(request, company):
    if is_admin(request, company):
        return HttpResponse("Create a panel")


@login_required
def add_members(request, company):
    if is_admin(request, company):
        return HttpResponse("Add collaborators")


@login_required
def add_notice(request, company):
    if is_admin(request, company):
        return HttpResponse("Add a notice")


@login_required
def view_candidates(request, company):
    if company_auth(request, company):
        return HttpResponse("View Candidate")


@login_required
def rdrive_edit(request,company):
    if is_admin(request, company):
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


@login_required
def company_auth(request, company):
    user = request.user
    company = Company.objects.get(name=company)
    if Collaborator.objects.filter(hr=user, company=company).exists() or \
        CompanyAdmin.objects.filter(admin=user, company=company).exists():
        return True
    else:
        return False


def company_exists(company):
    if Company.objects.filter(name=company).exists():
        return True
    else:
        return False


def is_admin(request, company):
    user = request.user
    company = Company.objects.get(name=company)
    if CompanyAdmin.objects.filter(admin=user, company=company).exists():
        return True
    else:
        return False


