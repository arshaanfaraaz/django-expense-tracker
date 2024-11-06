from django.shortcuts import render, redirect
from django.contrib import messages
from tracker.models import *
from django.db.models import Sum

# Create your views here.
def home(request):
    if request.method == 'POST':
        data = request.POST
        description = data.get('description')
        amount = data.get('amount')
        
        if description is None:
            messages.error(request, 'Description should not be empty')
            return redirect('/')
        
        try:
           amount = float(amount)
           
        except Exception as e:
            messages.error(request, 'Amount should be an integer')
            return redirect('/')
        
        Transaction.objects.create(
            description = description, 
            amount = amount
        )
        
        
        return redirect('/')

    context = {'transactions':  Transaction.objects.all(),
               'balance':Transaction.objects.aggregate(total_balance = Sum('amount'))['total_balance'] or 0,
               'income':Transaction.objects.filter(amount__gt = 0).aggregate(total_income = Sum('amount'))['total_income'] or 0,
               'expenses':Transaction.objects.filter(amount__lt = 0).aggregate(total_expenses = Sum('amount'))['total_expenses'] or 0,
               
               }    
    return render(request, 'index.html', context)


def delete_transaction(request, uuid):
    Transaction.objects.get(uuid = uuid).delete()
    return redirect('/')