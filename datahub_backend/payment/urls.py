from rest_framework import routers
from .views import SubscriptionViewSet, TransactionViewSet

router = routers.DefaultRouter()

router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'transactions', TransactionViewSet)
