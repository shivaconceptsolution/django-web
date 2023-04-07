from django.urls import path
from . import views

urlpatterns=[
  path('',views.home,name='home'),
  path('assignment',views.assignment,name='assignmnet'),
  path('login',views.login,name='login'),
  path('report',views.report,name='report')

]