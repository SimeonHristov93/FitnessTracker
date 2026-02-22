from django.urls import path
from . import views

app_name = 'progress'

urlpatterns = [
    path('', views.WorkoutLogListView.as_view(), name='log_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('log/', views.log_workout, name='log_workout'),
    path('log/<int:workout_id>/', views.log_workout, name='log_workout_with_id'),
    path('log/detail/<int:pk>/', views.log_detail, name='log_detail'),
    path('log/update/<int:pk>/', views.log_update, name='log_update'),
    path('log/delete/<int:pk>/', views.log_delete, name='log_delete'),
]