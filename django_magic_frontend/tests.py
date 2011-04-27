'''
You can run this tests in shell. Take position on the project folder and type:

python manage.py test django_magic_frontend
'''

from django.test import TestCase
from django_magic_frontend.models import GenericModel
from django.db import models

#~ Models
class TestModel(GenericModel):
    name=models.CharField(max_length=255)
    description=models.TextField()
    price=models.IntegerField()
    def __unicode__(self):
        return self.name+' ('+self._meta.verbose_name+')'    

class GenericModelTestCase(TestCase):
    def setUp(self):
        self.tm=TestModel.objects.create(name="lion", description="jose",price=3)
        self.tm.save()
        #~ self.book1=Book.objects.create(title="lion", author="jose")
    def testInheritance(self):
        #~ Arrange
        #~ Given a test model (tm)
        
        #~ Act
        url=self.tm.get_create_url()
        #~ Assert
        self.assertEqual(url,'/django_magic_frontend/testmodel/new/')
        
'''
assertEqual(a, b) 	a == b 	 
assertNotEqual(a, b) 	a != b 	 
assertTrue(x) 	bool(x) is True 	 
assertFalse(x) 	bool(x) is False 	 

2.7
assertIs(a, b) 	a is b 
assertIsNot(a, b) 	a is not b 
assertIsNone(x) 	x is None 
assertIsNotNone(x) 	x is not None 
assertIn(a, b) 	a in b 
assertNotIn(a, b) 	a not in b 
assertIsInstance(a, b) 	isinstance(a, b) 
assertNotIsInstance(a, b) 	not isinstance(a, b) 
'''
