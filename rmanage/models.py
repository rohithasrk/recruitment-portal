from django.db import models

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

class RecruitmentDrive(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
