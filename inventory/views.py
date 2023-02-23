from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import InventorySerializer
from .models import Inventory
from cloudinary.uploader import upload


# Create your views here.
class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [permissions.AllowAny]
    
    # def perform_create(self, serializer):
    #     image = self.request.data.get('image')
    #     uploaded_image = upload(image)
    #     image_url = uploaded_image['secure_url']
    #     serializer.save(image=image_url)
