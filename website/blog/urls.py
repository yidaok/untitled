from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.abc,name='abc'),
    url(r'index/',views.abc,name='abc'),
]