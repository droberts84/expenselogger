from expenselogger.models import Expense
from django.shortcuts import render
from django.http import HttpResponseRedirect
from expenselogger.forms import ExpenseForm
from django.core import serializers



def index(request):

    # get context for all expenses from helper
    context = all_expense_context_helper()

    # add blank form
    context['form'] = ExpenseForm()
    
    return render(request, 'expenselogger/index.html', context)
    
# post to create expenses
def create_expense(request):
	form = ExpenseForm(request.POST or None)
	if form.is_valid():
		expense = form.save()
		return HttpResponseRedirect('/')
	else:
		# get context of all expenses to support list below form
		context = all_expense_context_helper()
		# add form
		context['form'] = form

		#redisplay with error
		return render(request, 'expenselogger/index.html', context)


# helper function to get context for all expenses
def all_expense_context_helper():
	expense_list = Expense.objects.all().order_by('-date')

	"""
	serialize ALL expenses JSON to support submitting similar expenses in javascript

	All expenses are converted to prevent live remote call to get single expense
	from database upon user click event.
	If volume of expenses is high, this should be revaluated
	"""
	json_expenses = serializers.serialize('json', expense_list);

	return {'expense_list': expense_list, 'json_expenses': json_expenses}


