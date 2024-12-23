from rest_framework.routers import DefaultRouter
from .views import CustomerUserViewSet, DebtViewSet, ReturnDebtViewSet

router = DefaultRouter()
router.register(r'users', CustomerUserViewSet)
router.register(r'debts', DebtViewSet)
router.register(r'returns', ReturnDebtViewSet)

urlpatterns = router.urls
