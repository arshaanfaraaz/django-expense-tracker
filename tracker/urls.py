from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('delete-transaction/<uuid>', delete_transaction, name='delete-transaction')
]
