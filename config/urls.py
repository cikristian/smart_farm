from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from farms.views import FarmViewSet
from activities.views import ActivityViewSet
from finance.views import TransactionViewSet
from predictions.views import PredictionViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'farms', FarmViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'predictions', PredictionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ USER ROUTES
    path('api/users/', include('users.urls')),

    # ✅ AUTH
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),

    # ✅ API ROUTER
    path('api/', include(router.urls)),
]