from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register("", views.TelegramViewSet, basename="discord")

urlpatterns = router.urls
