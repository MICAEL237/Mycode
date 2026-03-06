from django.urls import path
from .views import*




urlpatterns =[
    path('create/', GoalsCreateView.as_view(), name='create'),
    path('update/<int:pk>/', GoalsUpdate.as_view(), name='updategoals'),
    path('delete/<int:pk>/', GoalsDelete.as_view(), name='deletegoals'),
    path('liste/', GoalsListView.as_view(), name='listsgoals'),

    path('updateetat/<int:pk>/', GoalsUpdateetat.as_view(), name='updatetat'),
    path('taches/<int:pk>/<str:section>', DetailGoalsView.as_view(), name='taches'),



]