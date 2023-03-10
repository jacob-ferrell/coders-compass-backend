from rest_framework import serializers
from .models import Goal, Skill

class GoalSerializer(serializers.ModelSerializer):
    sub_goals = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Goal
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'