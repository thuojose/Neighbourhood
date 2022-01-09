from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from django.conf.urls import url


app_name = "watch"   


urlpatterns = [
    path('', views.index, name = 'Index'),
    path("register", views.register, name="register"),
    path('notifications', views.notification, name='notifications'),
    path('blog', views.blog, name='blog'),
    path('health', views.health, name='health'),
    path('authorities', views.authorities, name='authorities'),
    path('businesses', views.businesses, name='businesses'),
    path('view/blog/', views.view_blog, name='view_blog'),
    path('my-profile/', views.my_profile, name='my-profile'),
    path('create/profile',views.create_profile, name='create-profile'),
    path('user/<str:username>', views.user_profile, name = 'user-profile'),
    path('update/profile', views.update_profile, name = 'update-profile'),
    path('new/blogpost', views.new_blogpost, name='new-blogpost'),
     
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
