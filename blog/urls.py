from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^index/',views.index,name='index'),

]