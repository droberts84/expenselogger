from expenselogger.models import Expense
from django.shortcuts import render
from django.http import HttpResponseRedirect
from expenselogger.forms import ExpenseForm

def index(request):
    expsense_list = Expense.objects.all().order_by('-date')
    form = ExpenseForm()
    context = {'expense_list': expsense_list, 'form': form}
    
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
		