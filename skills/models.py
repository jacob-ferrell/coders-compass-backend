from django.db import models
from django.conf import settings

class Skill(models.Model):

    name = models.CharField(max_length=50)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Goal(models.Model):

    name = models.CharField(max_length=255, null=True, blank=True)

    description = models.TextField()

    complete = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now=True)

    updated_at = models.DateTimeField(auto_now=True)

    skill = models.ForeignKey(Skill, null=False, blank=False, on_delete=models.CASCADE)

    parent_goal = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='sub_goals')

    """ def __str__(self):
        return self.name """