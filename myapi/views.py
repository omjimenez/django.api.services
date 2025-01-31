
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views herefrom rest_framework.decorators import api_view

@api_view(['GET'])
def hola_mundo(request):
    return Response({"mensaje": "Hola Mundo"})
