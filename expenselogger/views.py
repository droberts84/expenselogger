from expenselogger.models import Expense
from django.shortcuts import render
from django.http import HttpResponseRedirect
from expenselogger.forms import ExpenseForm
from django.core import serializers


def index(request):
    expense_list = Expense.objects.all().order_by('-date')
    form = ExpenseForm()
    
    """
    serialize ALL expenses JSON to support submitting similar expenses in javascript
    
    All expenses are converted to prevent live remote call to get single expense
    from database upon user click event.
    If volume of expenses is high, this should be revaluated
    """
    json_expenses = serializers.serialize('json', expense_list);

    

    context = {'expense_list': expense_list, 'form': form, 'json_expenses': json_expenses}
    
    return render(request, 'expenselogger/index.html', context)
    
# post to create expenses
def create_expense(request):
	form = ExpenseForm(request.POST or None)
	if form.is_valid():
		expense = form.save()
		return HttpResponseRedirect('/')
	else:
		#redisplay with error
		return render(request, 'expenselogger/index.html', {'form': form,})
