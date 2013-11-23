"""
Expense Logger test clases
"""
from django.core.urlresolvers import reverse
import datetime
from django.utils import timezone
from django.test import TestCase
from decimal import *
from expenselogger.models import Expense #import model


class ExpenseViewsTestCase(TestCase):
     
	def test_index(self):
		# test that url works
		resp = self.client.get(reverse('index'))
		self.assertEqual(resp.status_code, 200)
		self.assertTrue('Expense Logger' in resp.content)

		# form fields appear
		self.assertTrue('Name' in resp.content)
		self.assertTrue('Expense type' in resp.content)
		self.assertTrue('Amount' in resp.content)
		self.assertTrue('Date' in resp.content)



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
		resp = self.client.post(reverse('create'), {'name': 'Flight to ORD',
													'expense_type': 'F',
													'amount': 123.45})
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(resp.context['form'].errors['date'], [u'This field is required.'])

