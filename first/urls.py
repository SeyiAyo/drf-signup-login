from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include

from first import views

router = DefaultRouter()
router.register("", views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
urlpatterns += router.urls