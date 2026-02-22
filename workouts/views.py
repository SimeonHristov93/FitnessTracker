from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Workout
from .forms import WorkoutForm


class WorkoutListView(ListView):
    model = Workout
    template_name = 'workouts/workout_list.html'
    context_object_name = 'workouts'
    paginate_by = 9

    def get_queryset(self):
        queryset = Workout.objects.all()

        workout_type = self.request.GET.get('type')
        if workout_type:
            queryset = queryset.filter(workout_type=workout_type)

        difficulty = self.request.GET.get('difficulty')
        if difficulty:
            queryset = queryset.filter(difficulty=difficulty)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workout_types'] = Workout.WORKOUT_TYPES
        context['difficulty_levels'] = Workout._meta.get_field('difficulty').choices
        return context


class WorkoutDetailView(DetailView):
    model = Workout
    template_name = 'workouts/workout_detail.html'
    context_object_name = 'workout'


def workout_details(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    return render(request, 'workouts/workout_detail.html', {'workout': workout})


def workout_create(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save()
            return redirect('workouts:workout_detail', pk=workout.pk)
    else:
        form = WorkoutForm()
    return render(request, 'workouts/workout_form.html', {
        'form': form,
        'title': 'Create New Workout'
    })


def workout_update(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('workouts:workout_detail', pk=workout.pk)
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'workouts/workout_form.html', {
        'form': form,
        'title': f'Edit {workout.name}'
    })


def workout_delete(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == 'POST':
        workout.delete()
        return redirect('workouts:workout_list')
    return render(request, 'workouts/workout_confirm_delete.html', {'object': workout})


def workout_search(request):
    query = request.GET.get('q', '')
    workouts = Workout.objects.all()

    if query:
        workouts = workouts.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(workout_type__icontains=query)
        )

    return render(request, 'workouts/workout_search.html', {
        'workouts': workouts,
        'query': query
    })

