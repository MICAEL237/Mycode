from django.urls import path
from .views import*




urlpatterns =[
    path('create/', TaskcreateView.as_view(), name='createtache'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='updatetache'),
    path('update/<int:pk>/', StatusUpdateView.as_view(), name='updatestatus'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='deletetache'),
    path('lissession/<int:pk>/', TaskDeatilView.as_view(), name='lissession'),

]