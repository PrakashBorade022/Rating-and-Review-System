
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home)
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
