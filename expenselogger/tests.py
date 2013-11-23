"""
Expense Logger test clases
"""
from django.core.urlresolvers import reverse
import datetime
from django.utils import timezone
from django.test import TestCase
from expenselogger.models import Expense #import model


class ExpenseViewsTestCase(TestCase):
     
	def test_index(self):
		# test that url works
		resp = self.client.get(reverse('index'))
		self.assertEqual(resp.status_code, 200)
		self.assertTrue('Expense Logger' in resp.content)

	def test_good_expense_submission(self):

		resp = self.client.post(reverse('create'), {'name': 'Flight to ORD',
													'expense_type': 'F',
													'amount': 123.45,
													'date': timezone.now(),})
		self.assertEqual(resp.status_code, 302)

		# check attributes are storec correctly
		e = Expense.objects.get(name='Flight to ORD')
		self.assertEqual(e.amount, 123.45)
		self.assertEqual(e.expense_type, 'F')

		# still on index page
		self.assertTrue('Expense Logger' in resp.content)


	# assume all fields required
	def test_bad_expense_submissions(self):
         # Send no POST data.
		resp = self.client.post(reverse('create'))
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(resp.context['error_message'], "You didn't select a choice.")

		# Send no name
		resp = self.client.post(reverse('create'), {'expense_type': 'F',
													'amount': 123.45,
													'date': timezone.now(),})
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(resp.context['error_message'], "Please specify a name for the expense.")

		# No expense type specified
		resp = self.client.post(reverse('create'), {'name': 'Flight to ORD',
													'amount': 123.45,
													'date': timezone.now(),})
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(resp.context['error_message'], "Please specify a an expense type.")

		# No amount specified
		resp = self.client.post(reverse('create'), {'name': 'Flight to ORD',
													'expense_type': 'F',
													'date': timezone.now(),})
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(resp.context['error_message'], "Please specify an amount for your expense")

		# No amount specified
		resp = self.client.post(reverse('create'), {'name': 'Flight to ORD',
													'expense_type': 'F',
													'amount': 123.45})
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(resp.context['error_message'], "Please specify an amount for your expense")