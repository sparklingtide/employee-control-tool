from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register("", views.TelegramViewSet, basename="telegram")

urlpatterns = router.urls
