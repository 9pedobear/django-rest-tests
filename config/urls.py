from django.contrib import admin
from django.urls import path
from app.views import CarViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls


