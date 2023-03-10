from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import re
import openai

class ChatGPTView(APIView):
    openai.api_key = settings.OPENAI_API_KEY
    def get(self, request):
        model_engine = 'text-davinci-003'
        skill = request.GET.get('skill', '')
        prompt = 'Give me 5 important goals for learning' + ' ' + skill
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
        data = {'response': responseSplit  }
        return Response(data, status=status.HTTP_200_OK)
