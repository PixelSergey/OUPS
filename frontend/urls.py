from django.urls import path
from django.views.generic.base import RedirectView
from . import views

favicon_view = RedirectView.as_view(url="/static/favicon.ico", permanent=True)

urlpatterns = [
    path("", views.index, name="index"),
    path("send", views.send, name="send"),
    path("deliver", views.deliver, name="deliver"),
    path("favicon.ico", favicon_view),
]
