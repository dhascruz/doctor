from django.urls import path
# from .views import CartItemViews
# from .views import SalesItemViews
# from .views import AssociateItemViews
# from .views import TransactionItemViews

from . import views

urlpatterns = [
    #path('cart-items/', CartItemViews.as_view()),
 path('appointments', views.appointments, name='appointments'),


     
    
]