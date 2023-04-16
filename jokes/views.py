from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .serializers import JokeSerializer
from .models import Joke
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import requests
import math
import json
from django.http import JsonResponse
# Create your views here.
import random

@csrf_exempt
def get_random(request, type_joke=None):

    if type_joke is None:
        types = ['dad', 'chuck']
        type_joke = random.choice(types)
    if type_joke == 'chuck':
        response = requests.get('https://api.chucknorris.io/jokes/random')
        chuck_data = json.loads(response.text)
        data = {}
        data['text'] = chuck_data['value']
        data['type'] ='chuck'
        return JsonResponse(data, status=status.HTTP_200_OK)
    elif type_joke == 'dad':
        response = requests.get('https://icanhazdadjoke.com/slack')
        dad_data = json.loads(response.text)
        data = {}
        data['text'] = dad_data['attachments'][0]['text']
        data['type'] ='dad'
        return JsonResponse(data, status=status.HTTP_200_OK)
    else:
        data = {}
        data['error'] = "The parameter doesn't exist"
        return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt
def get_mcm(request):

    numbers = request.GET.getlist('numbers')
    if not all(num.isdigit() for num in numbers):
        data = {}
        data['error'] = "Invalid format"
        return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
    else:
        numbers = list(map(int, numbers))
        lcm = numbers[0]
        for num in numbers[1:]:
            gcd = math.gcd(lcm, num)
            lcm = lcm * num // gcd
        data = {}
        data['list'] = numbers
        data['mcm'] = lcm
        return JsonResponse(data, status=status.HTTP_200_OK)
       
@csrf_exempt
def get_plusone(request):

    number = request.GET.getlist('number')
    if not number.isdigit():
        data = {}
        data['error'] = "Invalid format"
        return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
    else:
        number = int(number)+1
        
        data = {}
        data['number'] = number
        data['plus_one'] = number
        return JsonResponse(data, status=status.HTTP_200_OK)
       


class JokeView(APIView):
    
    serializer_class = JokeSerializer
    
    def get(self, request, *args, **kwargs):
        
        products = Joke.objects.all()
        print(products)
        serializer = self.serializer_class(products, many=True)
        
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
       
        data = {
            'text': request.data.get('text'), 
            'type': request.data.get('type'), 
        }
        serializer = JokeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class JokeViewbyId(APIView):

    def get_object(self, joke_id):
        
        try:
            return Joke.objects.get(id=joke_id)
        except Joke.DoesNotExist:
            return None

    def get(self, request, joke_id, *args, **kwargs):
       
        jokeInstance = self.get_object(joke_id)
        if not jokeInstance:
            return Response(
                {"error": "Object with that id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = JokeSerializer(jokeInstance)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, joke_id, *args, **kwargs):
       
        jokeInstance = self.get_object(joke_id)
        if not jokeInstance:
            return Response(
                {"error": "Object with that id does not exist"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'text': request.data.get('text'), 
            'type': request.data.get('type'), 
        }
        serializer = JokeSerializer(instance = jokeInstance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, joke_id, *args, **kwargs):
       
        jokeInstance = self.get_object(joke_id, request.user.id)
        if not jokeInstance:
            return Response(
                {"error": "Object with that id does not exist"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        jokeInstance.delete()
        return Response(
            {"response": "Object deleted succesfully"},
            status=status.HTTP_200_OK
        )