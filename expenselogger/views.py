from expenselogger.models import Expense
from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    expsense_list = []  #implement me
    context = {'expense_list': expsense_list}
    return render(request, 'expenselogger/index.html', context)
    
# post to create expenses
def create_expense(request):
	try:
		e = Expense(name=request.POST['name'],
					expense_type=request.POST['expense_type'],
					amount=request.POST['amount'],
					date=request.POST['date'],)
	except (KeyError):
		#redisplay with error
		return render(request, 'index', {'error_message': "fields missing"})
	else:
		e.save()
		return HttpResponseRedirect('index')