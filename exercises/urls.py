from django.urls import path
from . import views

app_name = 'exercises'

urlpatterns = [
    path('', views.ExerciseListView.as_view(), name='exercise_list'),
    path('create/', views.exercise_create, name='exercise_create'),
    path('<int:pk>/edit/', views.exercise_update, name='exercise_update'),
    path('<int:pk>/delete/', views.exercise_delete, name='exercise_delete'),
]
