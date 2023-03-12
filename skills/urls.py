from django.urls import path
from .views import GoalView, SkillView

app_name = 'skills'

urlpatterns = [
    path('goal/', GoalView.as_view()),
    path('', SkillView.as_view()),
    
]
