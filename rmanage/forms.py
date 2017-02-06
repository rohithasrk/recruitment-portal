from django import forms
import django.db.models.options as options

from rmanage.models import *

options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('fields',)

class CompanyForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Company
        fields = ['name', 'email', 'password']

class ApplicantForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Applicant
        fields = ['name', 'email', 'password']

class ApplicantDetailForm(forms.ModelForm):
    class Meta:
        model = ApplicantDetail
        fields = ['company', 'phone_no', 'resume', 'role']

class RecruitmentDriveForm(forms.ModelForm):
    end_date = forms.DateField(widget=forms.DateInput())
    class Meta:
        model = RecruitmentDrive
        fields = ['name', 'role', 'end_date']

class RoundForm(models.Model):
    class Meta:
        fields = ['name', 'role']

class PanelForm(models.Model):
    class Meta:
        fields = ['name', 'rdrive', 'round_info']

class CollaboratorForm(models.Model):
    class Meta:
        fields = ['panel', 'phone_no']
