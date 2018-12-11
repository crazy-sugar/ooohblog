from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import static
from rest_framework.routers import SimpleRouter

from backweb import views
from ooohblog.settings import MEDIA_URL, MEDIA_ROOT

router = SimpleRouter()



urlpatterns = [
    url(r'^login/', views.user_login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^my_index/', views.my_index, name='my_index'),
    url(r'^article/', views.article, name='article'),
    url(r'^add_article/', views.add_article, name='add_article'),
    url(r'^article_list/', views.article_list, name='article_list'),
    url(r'^logout/', auth_views.logout, name='user_logout'),
    url(r'^del_article/(\d+)/',views.del_article,name='del_article'),
    url(r'^edit_article/(?P<id>\d+)/',views.edit_article,name='edit_article'),
]

urlpatterns += router.urls
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)