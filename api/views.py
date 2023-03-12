from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from skills.models import Skill
import re
import openai


class ChatGPTView(APIView):
    openai.api_key = settings.OPENAI_API_KEY

    def get(self, request):
        model_engine = 'text-davinci-003'
        skill = request.GET.get('skill', '')
        goal = request.GET.get('goal', '')
        prompt = 'Give me 5 important goals for learning' + ' ' + skill
        if goal is not None:
            skill_name = Skill.objects.get(id=skill).name
            prompt = 'Break down the following goal for learning ' + \
                skill_name + ' into 5 sub-goals:' + goal
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
        print(data)
        return Response(data, status=status.HTTP_200_OK)
