from rest_framework.routers import DefaultRouter

from . import views

app_name = 'food'

router = DefaultRouter()
router.register('fruits', views.FruitViewSet)
router.register('vegetables', views.VegetableViewSet)

urlpatterns = router.urls
