from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import InventorySerializer
from .models import Inventory
from cloudinary.uploader import upload
from cloudinary import api
from cloudinary.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [permissions.AllowAny]
    
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # Retrieve the public_id of the image from the model instance
        image_public_id = instance.image.public_id
        try:
            # Delete the image from Cloudinary
            api.delete_resources([image_public_id])
        except NotFound:
            # Handle case when image is not found on Cloudinary
            pass
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    

