from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rating.views import RatingViewSet, comic_rating

router = DefaultRouter()
router.register(r'ratings', RatingViewSet, basename='rating')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/comics/<int:comic_id>/rating/', comic_rating, name='comic-rating'),
]