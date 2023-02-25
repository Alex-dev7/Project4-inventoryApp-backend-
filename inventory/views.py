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
        # Retrieve the public_id of the image 
        image_public_id = instance.image.public_id
        try:
            # Delete the image from cloudinary
            api.delete_resources([image_public_id])
        except NotFound:
            # Handle case when image is not found on cloudinary
            pass
        self.perform_destroy(instance) # proced with deletion of the record form the database
        return Response(status=status.HTTP_204_NO_CONTENT)  #  class that is used to return a response to an HTTP request
    

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.pop('partial', False))
        serializer.is_valid(raise_exception=True)

        
        if 'image' in request.data:
            image_public_id = instance.image.public_id
            try:
                api.delete_resources([image_public_id])
            except NotFound:
                pass

            # Upload the new image to cloudinary and update the model instance with the new image URL
            uploaded_image = upload(request.data['image'])
            request.data['image'] = uploaded_image['secure_url']
        
        self.perform_update(serializer)
        return Response(serializer.data)
