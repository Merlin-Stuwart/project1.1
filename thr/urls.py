from django.urls import path
from thr.views import *

app_name='name2'
urlpatterns=[
    path('thr1/',thr1,name='thr1'),
    path('thr2/',thr2,name='thr2'),
]