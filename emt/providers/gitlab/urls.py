from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register("", views.GitlabViewSet, basename="gitlab")

urlpatterns = router.urls
