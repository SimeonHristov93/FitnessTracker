from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .forms import ExerciseForm
from .models import Exercise

class ExerciseListView(ListView):
    model = Exercise
    template_name = 'exercises/exercise_list.html'
    context_object_name = 'exercises'

def exercise_create(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workouts:workout_list')
    else:
        form = ExerciseForm()
    return render(request, 'exercises/exercise_form.html', {'form': form})

def exercise_update(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('exercises:exercise_list')
    else:
        form = ExerciseForm(instance=exercise)
    return render(request, 'exercises/exercise_form.html', {'form': form})

def exercise_delete(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        exercise.delete()
        return redirect('exercises:exercise_list')
    return render(request, 'exercises/exercise_confirm_delete.html', {'exercise': exercise})
