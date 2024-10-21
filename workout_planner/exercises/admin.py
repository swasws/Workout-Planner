from django.contrib import admin
from .models import Exercise, WorkoutPlan, WorkoutDay, WorkoutExercise

admin.site.register(Exercise)
admin.site.register(WorkoutPlan)
admin.site.register(WorkoutDay)
admin.site.register(WorkoutExercise)