from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('polls.views',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    url(r'^$', 'index', name='index'),
    url(r'^(?P<poll_id>\d+)/$', 'detail', name='detail'),
    url(r'^(?P<poll_id>\d+)/results/$', 'results', name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'vote', name='vote'),
)
