from rest_framework import routers
from django.conf import settings
from works_single_view.api.views import (
    WorkViewSet,
    ContributorViewSet,
)

if settings.DEBUG:
    router = routers.DefaultRouter()
else:
    router = routers.SimpleRouter()

router.register(r"works", WorkViewSet)
router.register(r"contributors", ContributorViewSet)

urlpatterns = router.urls
