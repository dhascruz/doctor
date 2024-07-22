import locale
import os
from django.contrib.staticfiles.storage import staticfiles_storage




inv_url = staticfiles_storage.url('')
from django.conf import settings
from io import BytesIO
from django.db import IntegrityError
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, Protection
from . import renderers
from dateutil.relativedelta import relativedelta
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Count
#from .models import Associate, Document, Ajax, CsvUpload
#from pasumai_api.models import Associate, Document, Ajax, CsvUpload
from doctor.models import *
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *

from datetime import datetime, date
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from core.forms import *
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from pathlib import Path

from decimal import Decimal




#from crud.tables import *

# Create your views here.
@login_required
def index(request):
    app_list = Appointment.objects.all()
    # rev_cnt=Transactions.objects.filter(status=1).all().count()
    # sal_cnt=Transactions.objects.filter(status=2).all().count()
    # sub_cnt=Transactions.objects.filter(status=3).all().count()
    # sto_cnt=Transactions.objects.filter(status=4).all().count()

    paginator = Paginator(app_list, 2000)
    page = request.GET.get('page')
    try:
        sales = paginator.page(page)
    except PageNotAnInteger:
        sales = paginator.page(1)
    except EmptyPage:
        sales = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'sales': sales})
    

#### assocaite view start

@login_required
def app_list(request):
    appointments_list = Appointment.objects.all()
    
    paginator = Paginator(appointments_list, 5)
    page = request.GET.get('page')
    try:
        appointments = paginator.page(page)
    except PageNotAnInteger:
        appointments = paginator.page(1)
    except EmptyPage:
        appointments = paginator.page(paginator.num_pages)
    return render(request, 'app_list.html', {'appointments': appointments})


@login_required
def app_create(request):
    if request.method == 'POST':
    
        form = AppointmentForm(request.POST)
        if form.is_valid():
                form.save()
                return redirect('appointment_success')

                messages.success(request, 'appointment was created successfully!')
                return redirect('/app_list')
    else:
        
            form = AppointmentForm()        
            return render(request, 'app_create.html' , {'form': form})


@login_required
def app_edit(request, pk):
    # doctors = doctor.objects.get(id=id)
    # context = {'doctors': doctors}
    # return render(request, 'doc_edit.html', context)

    item = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('app_list')
    else:
        form = AppointmentForm(instance=item)
    return render(request, 'doc_edit.html', {'form': form})


@login_required
def success(request):
    return render(request, 'success.html')

@login_required
def appointment_success(request):
    return render(request, 'app_success.html')


@login_required
def app_update(request, id):
    appointment = appointment.objects.get(id=id)
    appointment.name=request.POST['name']
    appointment.add_street=request.POST['street']
    appointment.add_location=request.POST['location']
    appointment.add_district=request.POST['district']
    appointment.add_state=request.POST['state']
    appointment.add_pincode=request.POST['pincode']
    appointment.phone=request.POST['phone']
    # appointment.name = request.POST['name']
    # appointment.lastname = request.POST['lastname']
    # appointment.mobile_number = request.POST['mobile_number']
    # appointment.description = request.POST['description']
    # appointment.location = request.POST['location']
    # appointment.date = request.POST['date']
    appointment.save()
    messages.success(request, 'appointment was updated successfully!')
    return redirect('/app_list')

@login_required
def app_delete(request, id):
    appointment = appointment.objects.get(id=id)
    appointment.delete()
    messages.warning(request, 'appointment was deleted successfully!')
    return redirect('/list')

#### assocaite view end



####doctor view start

@login_required
def doc_list(request):
    doctors_list = Doctor.objects.all()
    
    paginator = Paginator(doctors_list, 5)
    page = request.GET.get('page')
    try:
        doctors = paginator.page(page)
    except PageNotAnInteger:
        doctors = paginator.page(1)
    except EmptyPage:
        doctors = paginator.page(paginator.num_pages)
    return render(request, 'doc_list.html', {'doctors': doctors})


@login_required
def doc_create(request):
    if request.method == 'POST':
    
        form = DoctorForm(request.POST)
        if form.is_valid():
                form.save()
                return redirect('doctor_success')

                
                #return redirect('/doc_list')
    else:
        
            form = DoctorForm()        
            return render(request, 'doc_create.html' , {'form': form})

@login_required
def doctor_success(request):
    return render(request, 'doc_success.html')

@login_required
def doc_edit(request, pk):
    # doctors = doctor.objects.get(id=id)
    # context = {'doctors': doctors}
    # return render(request, 'doc_edit.html', context)

    item = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('doc_list')
    else:
        form = DoctorForm(instance=item)
    return render(request, 'doc_edit.html', {'form': form})


@login_required
def doc_update(request, id):
    doctor = doctor.objects.get(id=id)
    doctor.name=request.POST['name']
    doctor.add_street=request.POST['street']
    doctor.add_location=request.POST['location']
    doctor.add_district=request.POST['district']
    doctor.add_state=request.POST['state']
    doctor.add_pincode=request.POST['pincode']
    doctor.phone=request.POST['phone']
    # doctor.name = request.POST['name']
    # doctor.lastname = request.POST['lastname']
    # doctor.mobile_number = request.POST['mobile_number']
    # doctor.description = request.POST['description']
    # doctor.location = request.POST['location']
    # doctor.date = request.POST['date']
    doctor.save()
    messages.success(request, 'doctor was updated successfully!')
    return redirect('/doc_list')

@login_required
def doc_delete(request, id):
    doctor = doctor.objects.get(id=id)
    doctor.delete()
    messages.warning(request, 'doctor was deleted successfully!')
    return redirect('/list')

####doctor view end
