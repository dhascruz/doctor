from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    
    ##associagte
    path('app_create', views.app_create, name='app_create'),
    path('app_list', views.app_list, name='app_list'),
    path('app_edit/<int:pk>/edit/', views.app_edit, name='app_edit'),
    path('app_delete/<int:id>', views.app_delete, name='app_delete'),
    #path('success/', success, name='success'),
    
    path('doctor_success/', views.doctor_success, name='doctor_success'),



    path('doc_create', views.doc_create, name='doc_create'),
    path('doc_list', views.doc_list, name='doc_list'),
    path('doc_edit/<int:pk>/edit/', views.doc_edit, name='doc_edit'),
    path('doc_edit/update/<int:id>', views.doc_update, name='doc_update'),
    path('doc_delete/<int:id>', views.doc_delete, name='doc_delete'),


    path('pat_create', views.pat_create, name='pat_create'),
    path('pat_list', views.pat_list, name='pat_list'),
    path('pat_edit/<int:pk>/edit/', views.pat_edit, name='pat_edit'),
    path('pat_edit/update/<int:id>', views.pat_update, name='pat_update'),
    path('pat_delete/<int:id>', views.pat_delete, name='pat_delete'),


    path('new_patient/', views.new_patient, name='new_patient'),
    path('new_appointment/', views.new_appointment, name='new_appointment'),
    path('patient_success/', views.patient_success, name='patient_success'),
    path('appointment_success/', views.appointment_success, name='appointment_success'),
    path('appointment_details/', views.appointment_details, name='appointment_details'),
    path('approved_patient_details/', views.approved_patient_details, name='approved_patient_details'),
    path('schedule/', views.schedule, name='schedule'),
    path('reports/', views.reports, name='reports'),

    path('update_status/<int:appointment_id>/<str:status>/', views.update_status, name='update_status'),

    path('doctors/<int:doctor_id>/book/', views.book_appointment, name='book_appointment'),


    # path('sales_create', views.sales_create, name='sales_create'),
    # path('sales_list', views.sales_list, name='sales_list'),
    # path('sales_listnew', views.sales_listnew, name='sales_listnew'),
    # path('sales_edit/<int:id>', views.sales_edit, name='sales_edit'),
    # path('sales_edit/update/<int:id>', views.sales_update, name='sales_update'),
    # path('sales_delete/<int:id>', views.sales_delete, name='sales_delete'),
    # path('sales_excel', views.sales_to_excel, name='sales_excel'),
    # path('invoice_excel', views.invoices_to_excel, name='invoice_excel'),

    # path('sales_export_xls', views.sales_export_xls, name='sales_export_xls'),


    # path('trans_create', views.trans_create, name='trans_create'),
    # path('trans_list', views.trans_list, name='trans_list'),
    # path('trans_edit/<int:id>', views.trans_edit, name='trans_edit'),
    # path('trans_edit/update/<int:id>', views.trans_update, name='trans_update'),
    # path('trans_delete/<int:id>', views.trans_delete, name='trans_delete'),
    # path('inv_create/<int:id>', views.inv_create, name='inv_create'),
    # path('inv_pdf/<int:id>', views.inv_rep_pdf, name='inv_pdf'),
    
    # path('invoices_list', views.invoices_list, name='invoices_list'),
    # path('invoice_edit/<int:id>', views.invoice_edit, name='invoice_edit'),
    # path('invoice_edit/update/<int:id>', views.invoice_update, name='invoice_update'),



    # path('trans_list_byid/<int:id>', views.trans_list_byid, name='trans_list_byid'),
    # path('trans_list_bystatus/<int:id>', views.trans_list_bystatus, name='trans_list_bystatus'),
    
    
    
    
    # path('ajax/', views.ajax, name='ajax'),
    # path('ajax/ajax', views.ajax, name='ajaxpost'),
    # path('ajax/delete', views.ajax_delete, name='ajax_delete'),
    # path('ajax/getajax', views.getajax, name='getajax'),
#     path('register', views.register, name='register'),
#     path('register/success/', views.register_success, name='register_success'),
 ]
