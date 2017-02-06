from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    
    def __str__(self):
       return self.name

class Applicant(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
       return self.name



class ApplicantDetail(models.Model):
    applicant = models.ForeignKey(Applicant)
    company = models.ForeignKey(Company)
    phone_no = models.CharField(max_length=15)
    resume = models.FileField(upload_to='resume/')
    role = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
       return self.applicant.name


class RecruitmentDrive(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    date_created = models.DateField()
    end_date = models.DateField()

    def __str__(self):
      return "%s- %s" %(self.company.name, self.name)

   
class Round(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company)
    recruitment_drive = models.ForeignKey(RecruitmentDrive)
    role = models.CharField(max_length=100)

    def __str__(self):
       return "%s- %s  Round: %s" %(self.company.name, self.recruitment_drive.name, self.name)


class Panel(models.Model):
    name = models.CharField(max_length=100)
    current_candidate = models.ForeignKey(Applicant, null=True)
    rdrive = models.ForeignKey(RecruitmentDrive)
    round_info = models.ForeignKey(Round)

    def __str__(self):
       return self.name


class Collaborator(models.Model):
    hr = models.OneToOneField(User)
    company = models.ForeignKey(Company)
    panel = models.ManyToManyField(Panel)
    phone_no = models.CharField(max_length=15)

    def __str__(self):
       return self.name


class Score(models.Model):
    applicant = models.ForeignKey(Applicant)
    panel = models.ForeignKey(Panel)
    score = models.IntegerField(default=0)

    def __str__(self):
       return self.name


