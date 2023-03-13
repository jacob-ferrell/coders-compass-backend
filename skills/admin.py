from django.contrib import admin
from .models import Goal, Skill

class SkillAdmin(admin.ModelAdmin):
    list_display=('id', 'name')

class GoalAdmin(admin.ModelAdmin):
    list_display=('id', 'description', 'skill', 'complete')
admin.site.register(Goal, GoalAdmin)
admin.site.register(Skill, SkillAdmin)
