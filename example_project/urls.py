from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^catalog/', include('example_project.catalog.urls')),
	(r'^$', 'catalog.views.index' ,{},'homepage'),
)
