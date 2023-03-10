from django.urls import path
from .views import GoalView, SkillView

app_name = 'skills'

urlpatterns = [
    path('', SkillView.as_view()),
    path('goal/', GoalView.as_view()),
]
