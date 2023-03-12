from rest_framework import serializers
from .models import Goal, Skill


class GoalSerializer(serializers.ModelSerializer):
    sub_goals = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Goal
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
