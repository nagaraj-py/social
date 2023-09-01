from rest_framework.routers import DefaultRouter
from Ecartapp.api.views import ProductView

router = DefaultRouter()
router.register(r'products',ProductView, basename='products')

urlpatterns = router.urls