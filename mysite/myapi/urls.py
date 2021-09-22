from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'images', views.ImageViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'index/', views.index, name='index'),
    url(r'search/', views.search, name='index'),
]