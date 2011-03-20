from django.db import models
from django.core.urlresolvers import reverse

from django_magic_frontend.models import GenericModel
from django_magic_frontend.models import EditableAutoDateField
from django_magic_frontend.models import fill_choices

class Category(GenericModel):
    title=models.CharField(max_length=255)
    def __unicode__(self):
        return self.title+' ('+self._meta.verbose_name+')'
        
class Product(GenericModel):
    category=models.ForeignKey(Category)
    name=models.CharField(max_length=255)
    description=models.TextField()
    price=models.IntegerField()
    published=models.BooleanField()
    def __unicode__(self):
        return self.name+' ('+self._meta.verbose_name+')'

'''
In [1]: from catalog.models import  MyModel

In [2]: m=Product()

In [3]: m.id=3

In [4]: m.get_create_url()
Out[4]: '/catalog/product/new/'

In [5]: m.get_delete_url()
Out[5]: '/catalog/product/3/delete'

In [6]: m.get_index_url()
Out[6]: '/catalog/product/'

In [7]: m.get_update_url()
Out[7]: '/catalog/product/3/update'

and now with a child class

In [1]: from catalog.models import Product

In [2]: d=Product()

In [3]: d.id=4

In [4]: d.get
d.get_absolute_url  d.get_create_url    d.get_delete_url    d.get_index_url     d.get_update_url    

In [4]: d.get_update_url()
Out[4]: '/catalog/product/4/update'

this are the generated urls 

^catalog/ ^product/(page/)?(?P<page>[0-9]+)?$
^catalog/ ^product/(?P<object_id>\d+)/$
^catalog/ ^new/product/$
^catalog/ ^product/(?P<object_id>\d+)/update$
^catalog/ ^product/(?P<object_id>\d+)/delete$
'''

