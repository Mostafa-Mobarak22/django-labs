from lib2to3.fixes.fix_input import context

from django.urls import path,include
from .views import *

urlpatterns = [
   path('list/',list_account,name='list_account'),
   path('',account_account,name='account_account'),
   path('update/<int:id>',update_account,name='update_account'),
   path('delete/<int:id>',delete_account,name='delete_account'),
   path('create/',create_account,name='create_account'),
   path('show/<int:id>',show_account,name='show_account'),

]