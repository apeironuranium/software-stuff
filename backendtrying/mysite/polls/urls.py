from django.conf.urls import url

from . import views

app_name = "polls"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="polls_index"),
    url(r'^credits/$', views.CreditsView.as_view(), name="credits"),
]
