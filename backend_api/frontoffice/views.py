from rest_framework.response import Response
from rest_framework.views import APIView


class Token(APIView):
    def post(self, request):
        return Response({'token': 'test123'})
