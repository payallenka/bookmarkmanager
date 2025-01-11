from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Bookmark
from rest_framework import status
from .serializers import *
import logging

logger = logging.getLogger(__name__)

class UserRegistrationView(APIView):
    def post(self, request):
        permission_classes = [] 
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            # Create a new user
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookmarkViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] 
    serializer_class = BookmarkSerializer

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BookmarkListView(APIView):
    permission_classes = [IsAuthenticated]  
    serializer_class = BookmarkSerializer

    def get(self, request):
        bookmarks = Bookmark.objects.filter(user=request.user)
        serializer = BookmarkSerializer(bookmarks, many=True)
        return Response(serializer.data)
