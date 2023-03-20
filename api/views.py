from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from skills.models import Skill, Goal
from django.db.models import Q
import re
import openai


class ChatGPTView(APIView):
    openai.api_key = settings.OPENAI_API_KEY

    def get(self, request):
        model_engine = 'text-davinci-003'
        skill = request.GET.get('skill', None)
        goal = request.GET.get('goal', None)
        prompt = (f'Give me 5 important goals for learning {skill}')
        if goal:
            skill_name = Skill.objects.get(id=skill).name
            other_goals = Goal.objects.filter(
                Q(skill=skill) & ~Q(description=goal))
            other_goals_descriptions = ''
            for other_goal in other_goals:
                other_goals_descriptions += other_goal.description + '\n'
            prompt = 'Break down the following goal for learning ' + \
                skill_name + ' into no more than 5 sub-goals:' + goal + '\n' + \
                'If the goal recommends making projects, give some project recommendations. The goals you suggest cannot be the same or similar to these other goals you have already suggested: ' + '\n' + other_goals_descriptions
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            temperature=0.5,
            max_tokens=1024,
            n=1,
            stop=None,
        )
        response = completion.choices[0].text
        responseSplit = re.split(r"\n\d[.]", response)[1:]
        data = {'response': responseSplit}
        return Response(data, status=status.HTTP_200_OK)
