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
        fields = ['phone_no']

class RecruitmentDriveForm(forms.ModelForm):
    end_date = forms.DateField(widget=forms.DateInput())
    class Meta:
        model = RecruitmentDrive
        fields = ['name', 'role', 'end_date']

class RoundForm(forms.ModelForm):
    class Meta:
        model = Round
        fields = ['name', 'role']

class PanelForm(forms.ModelForm):
    class Meta:
        model = Panel
        fields = ['name', 'rdrive', 'round_info']

class CollaboratorForm(forms.ModelForm):
    class Meta:
        model = Collaborator
        fields = ['panel', 'phone_no']

class NoticeForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Notice
        fields = ['title', 'text']
