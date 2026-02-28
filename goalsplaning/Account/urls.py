from django.urls import path
from .views import *


urlpatterns= [
    path('', RegisterViews.as_view(), name='register'),
    path('login', loginViewForm.as_view(), name='login'),
]