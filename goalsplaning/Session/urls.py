from django.urls import path
from .views import *


urlpatterns =[
    path('ouvrir/', sessionCreateView.as_view(), name='ouvrirsession'),
    path('terminer/<int:pk>/', sessionValideeView.as_view(), name='terminersession' )

]