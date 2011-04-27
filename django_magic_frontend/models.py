from django.db import models
from django.core.urlresolvers import reverse

import datetime

def fill_choices(range_values):
    '''
    builds a sequence of two-tuples
    '''
    back=[]
    for x in range_values:
        back.append((x,x))
    return back

#~ auto date field, but editable after saved
DateTimeField=models.DateTimeField
class EditableAutoDateField(DateTimeField):
    def __init__(self, verbose_name=None, name=None, auto_now=False, auto_now_add=False, **kwargs):
        DateTimeField.__init__(self, verbose_name, name,**kwargs)
        self.auto_now, self.auto_now_add = auto_now, auto_now_add
        if auto_now or auto_now_add:
            self.blank=True
    def pre_save(self, model_instance, add):
        #~ print add
        if self.auto_now or (self.auto_now_add and add):
            value = datetime.datetime.now()
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(DateTimeField, self).pre_save(model_instance, add)
    
#abstract Model... this is a master piece :B ... muehehehe
class GenericModel(models.Model):
    class Meta:
        abstract=True
    def get_absolute_url(self):
        return reverse(self.get_absolute_url_alias(),kwargs={'object_id':self.id})
    def get_create_url(self):
        return reverse(self.get_create_url_alias())
    def get_index_url(self):
        return "/%s/%s/page/" % (self._meta.app_label,self._meta.module_name)
    def get_delete_url(self):
        return reverse(self.get_delete_url_alias(),kwargs={'object_id':self.id})
    def get_update_url(self):
        return reverse(self.get_update_url_alias(),kwargs={'object_id':self.id})
    def get_absolute_url_regexp(self):
        return "^%s/(?P<object_id>\d+)/$" % (self._meta.module_name)
    def get_create_url_regexp(self):
        return '^%s/new/$' % (self._meta.module_name)
    def get_index_url_regexp(self):
        return "^%s/page/(?P<page>[0-9|last]+)?$" % (self._meta.module_name)
    def get_delete_url_regexp(self):
        return "^%s/(?P<object_id>\d+)/delete/$" % (self._meta.module_name)
    def get_update_url_regexp(self):
        return "^%s/(?P<object_id>\d+)/update/$" % (self._meta.module_name)
    def get_absolute_url_alias(self):
        return "%s_%s_absolute" % (self._meta.app_label,self._meta.module_name)
    def get_create_url_alias(self):
        return '%s_%s_create' % (self._meta.app_label,self._meta.module_name)
    def get_index_url_alias(self):
        return "%s_%s_index" % (self._meta.app_label,self._meta.module_name)
    def get_delete_url_alias(self):
        return "%s_%s_delete" % (self._meta.app_label,self._meta.module_name)
    def get_update_url_alias(self):
        return "%s_%s_update" % (self._meta.app_label,self._meta.module_name)
    def build_generic_CRUD_urls(self, model_class):
        from django.conf.urls.defaults import url, patterns
        return patterns('django.views.generic',
            url(self.get_index_url_regexp(), 'list_detail.object_list', {'queryset': model_class.objects.all(),'paginate_by':10,'extra_context':{'dummy_object':self,'opts':self._meta}},self.get_index_url_alias()),
            url(self.get_absolute_url_regexp(), 'list_detail.object_detail', {'queryset': model_class.objects.all(),'extra_context':{'opts':self._meta}},self.get_absolute_url_alias()),
            url(self.get_create_url_regexp(), 'create_update.create_object', {'model':model_class,'extra_context':{'opts':self._meta}},self.get_create_url_alias()),
            url(self.get_update_url_regexp(), 'create_update.update_object', {'model':model_class,'extra_context':{'opts':self._meta}},self.get_update_url_alias()),
            url(self.get_delete_url_regexp(), 'create_update.delete_object', {'model':model_class,'post_delete_redirect':self.get_index_url(),'extra_context':{'opts':self._meta}},self.get_delete_url_alias()),
        )
        
    def show_field_detail(self, field_name):
        field = self._meta.get_field_by_name(field_name)
        if field[2] and not field_name=='id' and not field_name.endswith('_ptr'):
            url=''
            value=getattr(self,field_name)
            if field[0].choices:
                gd=getattr(self,'get_%s_display'%field_name)
                value=gd()
            #if it is a ForeignKey
            try:
                url=value.get_absolute_url()
            except:
                pass
            return(field[0].verbose_name,value,url)
    def show_detail(self):
        #get_declared_fields
        d=[]
        for fn in self._meta.get_all_field_names():
            detail=self.show_field_detail(fn)
            if detail:
                d.append(detail)
        return d

