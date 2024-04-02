from django.urls import path
from sec.views import *
app_name='name1'

urlpatterns=[
    path('sec1/',sec1,name='sec1'),
    path('sec2/',sec2,name='sec2'),
]