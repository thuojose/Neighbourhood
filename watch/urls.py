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
     
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    