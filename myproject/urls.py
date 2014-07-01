from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
'''These are different. eg. namespace=...'''

# from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()

# urlpatterns = patterns('',
    # url(r'^polls/', include('polls.urls')),
    # url(r'^admin/', include(admin.site.urls)),
# )