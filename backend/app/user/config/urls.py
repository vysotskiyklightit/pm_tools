from django.urls import include, path
from rest_framework import routers
from user import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('users/me/', views.UserMe.as_view()),
    path('', include(router.urls)),
]
