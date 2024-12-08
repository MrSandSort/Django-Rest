from django.db import models
class ImageUpload(models.Model):
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)




