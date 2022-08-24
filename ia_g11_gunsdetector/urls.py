from django.contrib import admin
from django.urls import path, include
from net import urls as net_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(net_urls)),
]
