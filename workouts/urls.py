from django.urls import path
from . import views

app_name = 'workouts'

urlpatterns = [
    path('', views.WorkoutListView.as_view(), name='workout_list'),
    path('search/', views.workout_search, name='workout_search'),
    path('<int:pk>/', views.workout_details, name='workout_detail'),
    path('create/', views.workout_create, name='workout_create'),
    path('<int:pk>/edit/', views.workout_update, name='workout_update'),
    path('<int:pk>/delete/', views.workout_delete, name='workout_delete'),
]