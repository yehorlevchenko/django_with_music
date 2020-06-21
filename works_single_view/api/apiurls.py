from django.urls import include, path
from rest_framework import routers
from works_single_view.api.views import WorkViewSet

router = routers.DefaultRouter()
router.register(r'works', WorkViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('works/', WorkViewSet)
]