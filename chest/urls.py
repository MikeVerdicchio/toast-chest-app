from django.conf.urls import url

from .views import GetRandomView, HealthCheck, HomepageView

urlpatterns = [
    url(r"^$", HomepageView.as_view(), name="chest"),
    url(r"^health$", HealthCheck.as_view(), name="health-check"),
    url(r"^random.json$", GetRandomView.as_view(), name="random-toast"),
]
