from django.db import models

# Create your models here.

#from associates.models import models1




    




    




    



    

    
class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    patient_phone = models.CharField(max_length=20)
    patient_email = models.CharField(max_length=20)
    patient_address = models.CharField(max_length=200)
    patient_fees = models.DecimalField(max_digits=5, decimal_places=0)
    patient_fee_status = models.BooleanField()
    appointment_date = models.DateTimeField()


def __str__(self):
        return self.name