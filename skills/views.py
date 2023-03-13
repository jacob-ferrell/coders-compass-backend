from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Goal, Skill
from django.shortcuts import get_object_or_404
from .serializers import GoalSerializer, SkillSerializer

class GoalView(APIView):
    def get(self, request):
        skill = request.GET.get('skill')
        goals = Goal.objects.filter(skill=skill).distinct()
        serializer = GoalSerializer(goals, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        print(data)
        goals = data['goals']
        for goal in goals:
            print(goal)
            goal['skill'] = data['skill']
        serializer = GoalSerializer(data=goals, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)      
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        data = request.data
        new_goals = data['goals']
        goals = []
        print(new_goals)
        for new_goal in new_goals:
            goal_id = int(new_goal['id'])
            goal = get_object_or_404(Goal, id=goal_id)
            serializer = GoalSerializer(goal, data=new_goal)
            if serializer.is_valid():
                goals.append(serializer.save())
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serialized_goals = GoalSerializer(goals, many=True)
        return Response(serialized_goals.data, status=status.HTTP_200_OK)
    
    def delete(self, request):
        pk_ids = request.query_params.get('pk_ids', None)
        if pk_ids:
            for i in pk_ids.split(','):
                get_object_or_404(Goal, id=int(i)).delete()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class SkillView(APIView):
    def get(self, request):
        skills = Skill.objects.filter(user=request.user)
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()
        print(data)
        data['user'] = request.user.id
        serializer = SkillSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)