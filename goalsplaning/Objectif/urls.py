from django.urls import path
from .views import*




urlpatterns =[
    path('create/', GoalsCreateView.as_view(), name='create'),
    path('update/<int:pk>/', GoalsUpdate.as_view(), name='updategoals'),
    path('delete/<int:pk>/', GoalsCreateView.as_view(), name='deletegoals'),
    path('updateetat/<int:pk>/', GoalsUpdateetat.as_view(), name='updatetat'),


]