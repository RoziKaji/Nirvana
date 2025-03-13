from rest_framework.generics import RetrieveAPIView, CreateAPIView
from users.serializers import UserSerializer
from rest_framework.response import Response

# Create your views here.

class ProfileAPIView(RetrieveAPIView):
    def get(self, request):
        User = request.user
        serializer = UserSerializer(User)
        return Response (serializer.data)
    
class CreateUserAPIView(CreateAPIView):
    pass
    

