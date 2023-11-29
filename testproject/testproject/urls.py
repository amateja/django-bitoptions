try:
    from django.conf.urls import url as re_path
except ImportError:
    from django.urls import re_path
from django.contrib import admin

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
]
