from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from user_app.api.serializers import RegisterUserSerializer
from rest_framework.authentication import TokenAuthentication

@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def logout_view(request):
    if request.method == 'POST':
        logout = request.user.auth_token.delete()
        return Response({"message": "Logged out successfully!"})

