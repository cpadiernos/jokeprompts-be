import random
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Prompt
from .serializers import PromptSerializer

@api_view(['GET'])
def prompt_random(request):
    if request.method == 'GET':
        data = random.choice(Prompt.objects.all())
        serializer = PromptSerializer(data)
        return Response(serializer.data)