from django.conf.urls import url

from core import views

urlpatterns = [
    url(r'^$', views.search, name="index"),
    # url(r'^input/$', views.inp, name="prodip")
]
