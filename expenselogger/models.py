from django.db import models
from django.core import serializers

class Expense(models.Model):
	# choices for expense type fields
	EXPENSE_TYPES = ( 
		('F','Flight'),
		('C','Car Rental'),
		('H','Hotel'), )

	# table attributes
	name = models.CharField(max_length=100)
	expense_type = models.CharField(max_length=1, choices=EXPENSE_TYPES)
	amount = models.DecimalField(max_digits=7, decimal_places=2)
	date = models.DateField()

	# string representation as expense name
	def __unicode__(self):
		return self.name

	def to_json(self):
		return serializers.serialize('json', [self]);

