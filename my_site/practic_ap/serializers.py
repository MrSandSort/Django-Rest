from rest_framework import serializers
from .models import ImageUpload

class ImageUploaderSerializer(serializers.ModelSerializer):

    image_url= serializers.SerializerMethodField()
    class Meta:
        model= ImageUpload
        fields= ['id','image','uploaded_at','image_url']

        
    def get_image_url(self,obj):
        if obj.image:
            return obj.image.url
        return None