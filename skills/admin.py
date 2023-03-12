from django.contrib import admin
from .models import Goal, Skill
class SkillAdmin(admin.ModelAdmin):
    list_display=('id', 'name')
admin.site.register(Goal)
admin.site.register(Skill, SkillAdmin)
