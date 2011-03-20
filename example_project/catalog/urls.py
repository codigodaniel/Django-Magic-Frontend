#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from django.conf.urls.defaults import *
from catalog.models import Product, Category
from django_magic_frontend import tools

urlpatterns = patterns('catalog.views',
    url(r'^$', 'index', {},Product._meta.app_label),
)

urlpatterns += tools.build_generic_CRUD_urls((Product,Category))

#~ other examples:
#~ urlpatterns += patterns('django.views.generic',
  #~ url(cat.get_index_url_regexp(), 'list_detail.object_list', {'queryset': Cat.objects.all(),'paginate_by':10},cat.get_index_url_alias()),
  #~ url(cat.get_absolute_url_regexp(), 'list_detail.object_detail', {'queryset': Cat.objects.all()},cat.get_absolute_url_alias()),
  #~ url(cat.get_create_url_regexp(), 'create_update.create_object', {'model':Cat},cat.get_create_url_alias()),
  #~ url(cat.get_update_url_regexp(), 'create_update.update_object', {'model':Cat},cat.get_update_url_alias()),
  #~ url(cat.get_delete_url_regexp(), 'create_update.delete_object', {'model':Cat,'post_delete_redirect':cat.get_index_url()},cat.get_delete_url_alias()),
  #~ 
  #~ url(dog.get_index_url_regexp(), 'list_detail.object_list', {'queryset': Dog.objects.all(),'paginate_by':10},dog.get_index_url_alias()),
  #~ url(dog.get_absolute_url_regexp(), 'list_detail.object_detail', {'queryset': Dog.objects.all()},dog.get_absolute_url_alias()),
  #~ url(dog.get_create_url_regexp(), 'create_update.create_object', {'model':Dog},dog.get_create_url_alias()),
  #~ url(dog.get_update_url_regexp(), 'create_update.update_object', {'model':Dog},dog.get_update_url_alias()),
  #~ url(dog.get_delete_url_regexp(), 'create_update.delete_object', {'model':Dog,'post_delete_redirect':dog.get_index_url()},dog.get_delete_url_alias()),
#~ 
  #~ url(bird.get_index_url_regexp(), 'list_detail.object_list', {'queryset': Bird.objects.all(),'paginate_by':10},bird.get_index_url_alias()),
  #~ url(bird.get_absolute_url_regexp(), 'list_detail.object_detail', {'queryset': Bird.objects.all()},bird.get_absolute_url_alias()),
  #~ url(bird.get_create_url_regexp(), 'create_update.create_object', {'model':Bird},bird.get_create_url_alias()),
  #~ url(bird.get_update_url_regexp(), 'create_update.update_object', {'model':Bird},bird.get_update_url_alias()),
  #~ url(bird.get_delete_url_regexp(), 'create_update.delete_object', {'model':Bird,'post_delete_redirect':bird.get_index_url()},bird.get_delete_url_alias()),
  
#~ )

