from django.db import models
from django.utils import timezone

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


class Patient(models.Model):
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    MORNING = 'MORNING'
    AFTERNOON = 'AFTERNOON'
    SLOT_CHOICES = [
        (MORNING, 'Morning (10:00 AM to 01:00 PM)'),
        (AFTERNOON, 'Afternoon (02:00 PM to 06:00 PM)'),
    ]

    PENDING = 'Pending'
    APPROVED = 'Approved'
    CANCELLED = 'Cancelled'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (CANCELLED, 'Cancelled'),
    ]

    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    patient_id = models.CharField(max_length=50, blank=True, null=True)
    appointment_date = models.DateField()
    slot = models.CharField(max_length=10, choices=SLOT_CHOICES)
    email = models.EmailField()
    address = models.TextField()
    appointment_fees = models.DecimalField(max_digits=6, decimal_places=2, default=150.00)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)


def __str__(self):
        return f"{self.name} - {self.appointment_date} ({self.slot})"





class MyDoctor(models.Model):
    name = models.CharField(max_length=255)
    # Other fields like specialty, qualifications, etc.

class Booking(models.Model):
    doctor = models.ForeignKey(MyDoctor, on_delete=models.CASCADE)
    date = models.DateField()
    MORNING = 'M'
    EVENING = 'E'
    SLOT_CHOICES = [
        (MORNING, 'Morning'),
        (EVENING, 'Evening'),
    ]
    slot = models.CharField(max_length=1, choices=SLOT_CHOICES)
    time = models.TimeField()

    def __str__(self):
        return f"{self.doctor.name} - {self.date} - {self.get_slot_display()} at {self.time}"


