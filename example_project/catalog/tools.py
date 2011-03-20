'''
http://efreedom.com/Question/1-213237/Django-One-Use-Djangos-Update-Object-Generic-View-Edit-Forms-Inherited-Models
'''
from django.contrib.contenttypes.models import ContentType
from django.views.generic import create_update

def update_object_as_child(parent_model_class):
   """
   Given a base models.Model class, decorate a function to return  
   create_update.update_object, on the child class.

   e.g.
   @update_object(Animal)
   def update_object(request, object_id):
      pass

  kwargs should have an object_id defined.
  """

  def decorator(function):
      def wrapper(request, **kwargs):
          # may raise KeyError
          id = kwargs['object_id']

          parent_obj = parent_model_class.objects.get( pk=id )

          # following http://www.djangosnippets.org/snippets/1031/
          child_class = parent_obj.content_type.model_class()

          kwargs['model'] = child_class

          # rely on the generic code for testing/validation/404
          return create_update.update_object(request, **kwargs)
      return wrapper

  return decorator


'''
And in animals/views.py, I have:

from mysite.core.views.create_update import update_object_as_child

@update_object_as_child(Animal)
def edit_animal(request, object_id):
  pass
And in animals/urls.py, I have:

urlpatterns += patterns('animals.views',
  url(r'^edit/(?P<object_id>\d+)$', 'edit_animal', name="edit_animal"),
)
Now I only need a unique edit function for each base class, which is trivial to create with a decorator.

Hope someone finds that helpful, and I'd be delighted to have feedback.

'''
