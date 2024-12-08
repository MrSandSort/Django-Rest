from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import ImageUpload
from .serializers import ImageUploaderSerializer
from rest_framework.views import APIView

class ImageUploadView(APIView):

    def post(self,request, *args, **kwargs):
        if 'image' not in request.FILES:
            return Response({'error': 'No image Uploaded'}, status= status.HTTP_400_BAD_REQUEST)
        
        serializer=ImageUploaderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def get(self,request):
        images = ImageUpload.objects.all()
        serializers= ImageUploaderSerializer(images, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
