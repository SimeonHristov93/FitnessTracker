from django.contrib import admin
from django.urls import path, include
from progress.views import dashboard
from .views import custom_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('exercises/', include('exercises.urls')),
    path('workouts/', include('workouts.urls')),
    path('progress/', include('progress.urls')),
    path('custom-404/', custom_404, name='custom404'),
]

handler404 = 'FitnessTracker.views.custom_404'