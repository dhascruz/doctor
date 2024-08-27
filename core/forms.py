from django import forms
from doctor.models import *

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'specialization']



class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'mobile_number', 'email', 'address']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

       



class AppointmentForm(forms.ModelForm):


    # doctor = forms.ChoiceField(
        
    #     widget=forms.Select(attrs={'class': 'form-control'})
    # )
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    mobile_number = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    patient_id = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
   
    appointment_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class':'form-control'})
    )

    email = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
        
    appointment_fees = forms.DecimalField(
        initial=150.00,
        widget=forms.NumberInput(attrs={'readonly': 'readonly'})
    )        

    # patient_address = forms.CharField(
    #     max_length=200,
    #     widget=forms.TextInput(attrs={'class': 'form-control'})
    # )
    # patient_fees = forms.CharField(
    #     max_length=10,
    #     widget=forms.TextInput(attrs={'class': 'form-control'})
    # )
    class Meta:
        model = Appointment
        
        fields = ['name', 'mobile_number', 'patient_id', 'appointment_date', 'slot', 'email', 'address',  'appointment_fees']
    widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
        }
    

class BookingForm(forms.ModelForm):
        class Meta:
            model = Booking
            fields = ['date', 'slot', 'time']

        date = forms.DateField(widget=forms.SelectDateWidget(), initial=timezone.now())
        slot = forms.ChoiceField(choices=Booking.SLOT_CHOICES)
        time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))