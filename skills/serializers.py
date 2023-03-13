from rest_framework import serializers
from .models import Goal, Skill

class GoalListSerializer(serializers.ListSerializer):
    def update(self, queryset, validated_data):
        for index, goal_data in enumerate(validated_data):
            goal = queryset[index]
            self.child.update(goal, goal_data)

        return queryset

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
        list_serializer_class = GoalListSerializer
