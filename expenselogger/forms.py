from django.forms import ModelForm
from expenselogger.models import Expense

class ExpenseForm(ModelForm):
	class Meta:
		model = Expense
		fields = ['name', 'expense_type', 'amount', 'date']