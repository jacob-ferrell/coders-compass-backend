from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

import openai




class TestView(APIView):
    permission_classes=[AllowAny]
    openai.api_key = settings.OPENAI_API_KEY
    def get(self, request):
        model_engine = 'text-davinci-003'
        prompt = request.GET.get('prompt', '')
        completion = openai.Completion.create(
            engine=model_engine, 
            prompt=prompt,
            temperature=0.5,
            max_tokens=1024,
            n=1,
            stop=None,
        )
        response = completion.choices[0].text
        data = {'response': response  }
        return Response(data, status=status.HTTP_200_OK)
