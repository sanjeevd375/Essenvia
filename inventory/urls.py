from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register(r'product', InventoryView, basename='products')

urlpatterns = []
urlpatterns += router.urls