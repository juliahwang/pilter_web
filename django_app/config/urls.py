from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^', include('article.urls')),
    url(r'^admin/', admin.site.urls)
]

# Only serve static files from Django during development
# Use Google Cloud Storage or an alternative CDN for production
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
