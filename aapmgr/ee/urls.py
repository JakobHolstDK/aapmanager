from django.contrib import admin
from django.urls import path, include

from .views import home, define_runtime


urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the urls from the aapmgr app
    path('', home),
    path('runtime/', define_runtime),
]
