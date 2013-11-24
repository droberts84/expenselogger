"""
Expense Logger test clases
"""
from django.core.urlresolvers import reverse
import datetime
from django.utils import timezone
from django.test import TestCase
from decimal import *
from expenselogger.models import Expense #import model


"""
Creates an Expense based on passed parameters
days is an offset for date to set date relative to now
(negative for in the past, positive for in the future)
"""
def create_test_expense(name, e_type, amount, days):
	return Expense.objects.create(name=name, expense_type=e_type, amount=amount, 
			date=datetime.date.today() + datetime.timedelta(days=days))


class ExpenseViewsTestCase(TestCase):
     
	
	def test_index(self):
		# create test data (ideally should use fixtures)
		e3 = create_test_expense('Expense 3', 'H', 593.25, -15)
		e4 = create_test_expense('Expense 4', 'F', 400, -25)
		e2 = create_test_expense('Expense 2', 'C', 183.20, -5)
		e1 = create_test_expense('Expense 1', 'F', 200.00, -1)

		# test that url works
		resp = self.client.get(reverse('index'))
		self.assertEqual(resp.status_code, 200)
		self.assertTrue('Expense Logger' in resp.content)

		# form fields appear
		self.assertTrue('Name' in resp.content)
		self.assertTrue('Expense type' in resp.content)
		self.assertTrue('Amount' in resp.content)
		self.assertTrue('Date' in resp.content)


		# test that expense data is availible and appropriately ordered by date
		self.assertTrue('expense_list' in resp.context)
		self.assertQuerysetEqual(resp.context['expense_list'], 
			['<Expense: Expense 1>', '<Expense: Expense 2>', '<Expense: Expense 3>', 
			'<Expense: Expense 4>'])

		# make sure that the template renders the expense attributes
		self.assertTrue(e1.name in resp.content)
		self.assertTrue('Flight' in resp.content)
		self.assertTrue('200.00' in resp.content)




	# expenses can be submitted through POST action
	def test_good_expense_submission(self):

		resp = self.client.post(reverse('create'), {'name': 'Flight to ORD',
													'expense_type': 'F',
													'amount': 123.45,
													'date': '11/01/13',
													})
		self.assertEqual(resp.status_code, 302)

		# check attributes are storec correctly
		e = Expense.objects.get(name ='Flight to ORD')
		self.assertAlmostEqual(e.amount, Decimal(123.45))
		self.assertEqual(e.expense_type, 'F')



	"""
	Test validations on expense submissions
	- Assuming all fields are required
	- Further validations should be checked for blanks, etc
	"""
	def test_bad_expense_submissions(self):


		# Send no name
		resp = self.client.post(reverse('create'), {'expense_type': 'F',
													'amount': 123.45,
													'date': '11/15/13',})
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(resp.context['form'].errors['name'], [u'This field is required.'])

		# No expense type specified
		resp = self.client.post(reverse('create'), {'name': 'Flight to ORD',
													'amount': 123.45,
													'date': '11/15/13',})
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(resp.context['form'].errors['expense_type'], [u'This field is required.'])

		# No amount specified
		resp = self.client.post(reverse('create'), {'name': 'Flight to ORD',
													'expense_type': 'F',
													'date': '11/15/13',})
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(resp.context['form'].errors['amount'], [u'This field is required.'])

		# No date specified
		e1 = create_test_expense('Expense 1', 'F', 200.00, -1)
		resp = self.client.post(reverse('create'), {'name': 'Flight to ORD',
													'expense_type': 'F',
													'amount': 123.45})
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(resp.context['form'].errors['date'], [u'This field is required.'])
		# after error other expenses should appear on page
		self.assertTrue(e1.name in resp.content)
		self.assertTrue('Flight' in resp.content)
		self.assertTrue('200.00' in resp.content)

	

