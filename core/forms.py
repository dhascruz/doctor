from django import forms
from doctor.models import *

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'specialization']

class AppointmentForm(forms.ModelForm):
    appointment_date = forms.DateTimeField(
        widget=forms.TextInput(attrs={'class': 'form-control','type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )


    # doctor = forms.ChoiceField(
        
    #     widget=forms.Select(attrs={'class': 'form-control'})
    # )
    patient_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    patient_phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    patient_email = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    patient_address = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    patient_fees = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Appointment
        fields = ['doctor', 'patient_name', 'patient_phone','patient_email','patient_address','patient_fees','appointment_date']
