from django.conf.urls import url
from . import views

app_name="cats"
urlpatterns = [
   url(r'^$', views.base, name='home'),
   url(r'^facts$', views.cat_fact, name='facts'),
]
