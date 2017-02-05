from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=30)

class Applicant(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)

class ApplicantDetail(models.Model):
    applicant = models.ForeignKey(Applicant)
    company = models.ForeignKey(Company)
    phone_no = models.CharField(max_length=15)
    resume = models.FileField(upload_to='resume/')
    role = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

class RecruitmentDrive(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    date_created = models.DateField()
    end_date = models.DateField()
    
class Round(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company)
    role = models.CharField(max_length=100)

class Panel(models.Model):
    name = models.CharField(max_length=100)
    current_candidate = models.ForeignKey(Applicant)
    rdrive = models.ForeignKey(RecruitmentDrive)
    round_info = models.ForeignKey(Round)

class Collaborator(models.Model):
    hr = models.OneToOneField(User)
    company = models.ForeignKey(Company)
    panel = models.ManyToManyField(Panel)
    phone_no = models.CharField(max_length=15)

class Score(models.Model):
    applicant = models.ForeignKey(Applicant)
    panel = models.ForeignKey(Panel)
    score = models.IntegerField(default=0)
