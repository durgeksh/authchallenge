from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class Welcome(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response("<h1>Welcome to the my web application!")
