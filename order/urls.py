from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register(r'neworder', OrderView, basename='neworders')

urlpatterns = []
urlpatterns += router.urls