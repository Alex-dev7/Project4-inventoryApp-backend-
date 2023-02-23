from django.contrib import admin
from django.urls import path, include
from rest_framework import routers 
from inventory.views import InventoryViewSet


# new router 
router = routers.DefaultRouter()
# register the view set
router.register(r'inventory', InventoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    
]

