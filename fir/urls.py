from django.urls import path
from fir.views import *

app_name='name'
urlpatterns=[
    path('fir1/',fir1,name='fir1'),
    path('fir2/',fir2,name='fir2'),
]