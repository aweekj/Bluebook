from django.conf.urls import include, url
from django.contrib import admin

from mysite.views import HomeView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
]

