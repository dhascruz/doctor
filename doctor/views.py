from django.shortcuts import render,redirect
# Create your views here.
from datetime import datetime, timedelta
# from .serializers import CartItemSerializer
# from .serializers import SalesItemSerializer
# from .serializers import AssociatesItemSerializer
# from .serializers import TransactionsItemSerializer

import base64
import os
import locale
from .models import *
from core.forms import *

from django.contrib.staticfiles.storage import staticfiles_storage
 
#from .models import CartItem
from .models import *

def appointments(request):
    if request.method == 'POST':
    
        form = AppointmentForm(request.POST)
        if form.is_valid():
                form.save()
                return redirect('appointment_success')

                messages.success(request, 'appointment was created successfully!')
                return redirect('/app_list')
    else:
        
            form = AppointmentForm()        
            return render(request, 'appointment.html' , {'form': form})

