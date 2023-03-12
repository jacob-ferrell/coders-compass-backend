from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Goal, Skill
from .serializers import GoalSerializer, SkillSerializer


class GoalView(APIView):
    def get(self, request):
        skill = request.GET.get('skill')
        goals = Goal.objects.filter(skill=skill).distinct()
        serializer = GoalSerializer(goals, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        goals = data['goals']
        for goal in goals:
            goal['skill'] = data['skill']
        serializer = GoalSerializer(data=goals, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        data = request.data
        goal_id = data['id']
        try:
            goal = Goal.objects.get(id=goal_id)
        except Goal.DoesNotExist:
            return Response(f"Goal with id {goal_id} does not exist", status=status.HTTP_404_NOT_FOUND)
        serializer = GoalSerializer(goal, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
