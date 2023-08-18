from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import NoteSerializer
import json

# Create your views here.
@api_view(['GET'])
def guestView(request):
    guest = Guest.objects.all()
    serializ = NoteSerializer(guest,many=True)
    
    
    return Response(serializ.data)


@api_view(['POST'])
def guestCreate(request):
    data = json.loads(request.body)
    guest = Guest.objects.create(
        name = data['form']['name'],
        email = data['form']['email'],
        subject = data['form']['subject'],
        message = data['form']['message'],
        
    )
    print(data)
    # data = request.data
    
    # note =Guest.objects.create(
    #     name=data['name']
    # )
    
    
    
    
    
    return Response("serializ.data")