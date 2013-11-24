expenselogger
===========

A simple site for submitting expenses.


###Assumptions
- All fields are required
- Expense Name or Date is not unique
- No additional validations are defined, as long as something is present
- Number of expenses will be extremely low
- Expense should be highlighted when a user hovers, to indicate it is clickable
- All expenses will be entered in USD
- Expense amount will always be $100,000 

###Setup
- pip install Django
- python manage.py syncdb
- python manage.py runserver
- browse to http://localhost:8000

###Dependencies
- Tested using Python 2.7.5 and Django 1.6
- Uses Bootstrap 3.00 and JQuery 1.10 (included)
