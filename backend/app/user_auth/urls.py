from django.urls import path
from user_auth.views import (DecoratedTokenObtainPairView,
                             DecoratedTokenRefreshView)

urlpatterns = [
    path('token/', DecoratedTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', DecoratedTokenRefreshView.as_view(),
         name='token_refresh'),
]
