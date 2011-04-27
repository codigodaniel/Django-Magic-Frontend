from django.conf.urls.defaults import *
from django_magic_frontend import tools
from django_magic_frontend.tests import TestModel

urlpatterns = tools.build_generic_CRUD_urls((TestModel,))
