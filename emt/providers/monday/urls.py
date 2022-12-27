from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register("", views.MondayViewSet, basename="monday")

urlpatterns = router.urls
