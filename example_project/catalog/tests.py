'''
You can run this tests in shell. Take position on the project folder and type:

python manage.py test catalog
'''

from django.test import TestCase
from catalog.models import Product, Category

class CategoryTestCase(TestCase):
    def setUp(self):
        self.tc=Category.objects.create(title="category test")
        self.tc.save()
    def testCreateUrl(self):
        """
        Tests that we can get the CREATION url of a category model
        """
        #~ Arrange
        #~ Given a test category (self.tc)
        #~ Act
        url=self.tc.get_create_url()
        #~ Assert
        self.assertEqual(url,'/catalog/category/new/')
    def testAbsoluteUrl(self):
        """
        Tests that we can get the ABSOLUTE url of a category model
        """
        #~ Arrange
        #~ Given a test category (self.tc)
        #~ Act
        url=self.tc.get_absolute_url()
        #~ Assert
        self.assertEqual(url,'/catalog/category/1/')
    def testDetailUrl(self):
        """
        Tests that we can get the UPDATE url of a category model
        """
        #~ Arrange
        #~ Given a test category (self.tc)
        #~ Act
        url=self.tc.get_update_url()
        #~ Assert
        self.assertEqual(url,'/catalog/category/1/update/')
    def testListUrl(self):
        """
        Tests that we can get the LIST url of a category model
        """
        #~ Arrange
        #~ Given a test category (self.tc)
        #~ Act
        url=self.tc.get_index_url()
        #~ Assert
        self.assertEqual(url,'/catalog/category/page/')
        
'''
assertEqual(a, b)   a == b   
assertNotEqual(a, b)    a != b   
assertTrue(x)   bool(x) is True      
assertFalse(x)  bool(x) is False     
'''
