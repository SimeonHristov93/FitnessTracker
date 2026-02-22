from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.db.models import Sum, Avg, Count
from django.db.models.functions import TruncDate
from datetime import timedelta
from django.utils import timezone
from workouts.models import Workout
from .models import WorkoutLog
from .forms import WorkoutLogForm
import json


def log_workout(request, workout_id=None):
    initial = {}
    workout = None

    if workout_id:
        workout = get_object_or_404(Workout, pk=workout_id)
        initial['workout'] = workout

    if request.method == 'POST':
        form = WorkoutLogForm(request.POST, initial=initial)
        if form.is_valid():
            log = form.save()
            return redirect('progress:log_detail', pk=log.pk)
    else:
        form = WorkoutLogForm(initial=initial)

    return render(request, 'progress/log_form.html', {
        'form': form,
        'workout': workout
    })


class WorkoutLogListView(ListView):
    model = WorkoutLog
    template_name = 'progress/log_list.html'
    context_object_name = 'logs'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        logs = self.get_queryset()
        context['total_workouts'] = logs.count()

        total_minutes = logs.aggregate(Sum('duration_minutes'))['duration_minutes__sum'] or 0
        context['total_minutes'] = total_minutes

        avg_rating = logs.aggregate(Avg('rating'))['rating__avg']
        context['avg_rating'] = round(avg_rating, 1) if avg_rating else 0.0

        week_ago = timezone.now() - timedelta(days=7)
        context['weekly_count'] = logs.filter(completed_at__gte=week_ago).count()

        return context


def log_detail(request, pk):
    log = get_object_or_404(WorkoutLog, pk=pk)
    return render(request, 'progress/log_detail.html', {'log': log})


def log_update(request, pk):
    log = get_object_or_404(WorkoutLog, pk=pk)

    if request.method == 'POST':
        form = WorkoutLogForm(request.POST, instance=log)
        if form.is_valid():
            form.save()
            return redirect('progress:log_detail', pk=log.pk)
    else:
        form = WorkoutLogForm(instance=log)

    return render(request, 'progress/log_form.html', {
        'form': form,
        'log': log
    })


def log_delete(request, pk):
    log = get_object_or_404(WorkoutLog, pk=pk)

    if request.method == 'POST':
        log.delete()
        return redirect('progress:log_list')

    return render(request, 'progress/log_confirm_delete.html', {'log': log})


def dashboard(request):
    logs = WorkoutLog.objects.all()

    total_workouts = logs.count()
    total_minutes = logs.aggregate(Sum('duration_minutes'))['duration_minutes__sum'] or 0

    workout_stats = Workout.objects.annotate(
        log_count=Count('logs')
    ).order_by('-log_count')[:5]

    total_calories = logs.aggregate(Sum('calories_burned'))['calories_burned__sum'] or 0

    avg_rating = logs.aggregate(Avg('rating'))['rating__avg']

    today = timezone.now().date()
    week_ago = today - timedelta(days=6)

    dates = [(today - timedelta(days=i)) for i in range(6, -1, -1)]
    chart_labels = [date.strftime('%a') for date in dates]

    daily_data = {date: {'duration': 0, 'calories': 0} for date in dates}

    stats = logs.filter(completed_at__date__gte=week_ago).annotate(
        date=TruncDate('completed_at')
    ).values('date').annotate(
        total_duration=Sum('duration_minutes'),
        total_calories=Sum('calories_burned')
    ).order_by('date')

    for stat in stats:
        stat_date = stat['date']
        if stat_date in daily_data:
            daily_data[stat_date]['duration'] = stat['total_duration'] or 0
            daily_data[stat_date]['calories'] = stat['total_calories'] or 0

    chart_data_duration = [daily_data[date]['duration'] for date in dates]
    chart_data_calories = [daily_data[date]['calories'] for date in dates]

    context = {
        'total_workouts': total_workouts,
        'total_minutes': total_minutes,
        'total_hours': round(total_minutes / 60, 1),
        'total_calories': total_calories,
        'avg_rating': round(avg_rating, 1) if avg_rating else 0.0,
        'workout_stats': workout_stats,
        'recent_logs': logs[:5],
        'chart_labels': json.dumps(chart_labels),
        'chart_data_duration': json.dumps(chart_data_duration),
        'chart_data_calories': json.dumps(chart_data_calories),
    }

    return render(request, 'progress/dashboard.html', context)
