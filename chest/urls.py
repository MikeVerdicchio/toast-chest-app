from django.conf.urls import url

from .views import GetRandomView, HomepageView

urlpatterns = [
    url(r"^$", HomepageView.as_view(), name="chest"),
    url(r"^random.json$", GetRandomView.as_view(), name="random-toast"),
]
