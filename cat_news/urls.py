from django.conf.urls import url
from . import views
urlpatterns = [
   url(r'^$', views.base),
   url(r'^facts$', views.cat_fact),
]
