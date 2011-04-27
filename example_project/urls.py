from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^catalog/', include('example_project.catalog.urls')),
	(r'^$', 'catalog.views.index' ,{},'homepage'),

    #~ this is only for testing, uncomment this before run tests
	#~ (r'^django_magic_frontend/', include('django_magic_frontend.urls')),
)
