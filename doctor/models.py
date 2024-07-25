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

# class Appointment(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient_name = models.CharField(max_length=100)
#     patient_phone = models.CharField(max_length=20)
#     patient_email = models.CharField(max_length=20)
#     patient_address = models.CharField(max_length=200)
#     patient_fees = models.DecimalField(max_digits=5, decimal_places=0)
#     patient_fee_status = models.BooleanField(default=False)
#     appointment_date = models.DateTimeField()


class Appointment(models.Model):
    MORNING = 'MORNING'
    AFTERNOON = 'AFTERNOON'
    SLOT_CHOICES = [
        (MORNING, 'Morning (10:00 AM to 01:00 PM)'),
        (AFTERNOON, 'Afternoon (02:00 PM to 06:00 PM)'),
    ]

    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    patient_id = models.CharField(max_length=50, blank=True, null=True)
    appointment_date = models.DateField()
    slot = models.CharField(max_length=10, choices=SLOT_CHOICES)
    email = models.EmailField()
    address = models.TextField()
    appointment_fees = models.DecimalField(max_digits=6, decimal_places=2, default=150.00)


def __str__(self):
        return f"{self.name} - {self.appointment_date} ({self.slot})"


