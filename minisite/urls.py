from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from expenselogger import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #implemented directly in project root to avoid using expenselogger namespace
    url(r'^create/', views.create_expense, name='create'), 
    url(r'^admin/', include(admin.site.urls)),
)
