from django.test import TestCase
from search.models import Book, Category
from django.db.utils import IntegrityError

class TestSearchModels(TestCase):
    """ Test search models """

    def setUp(self):
        """Model test set up """
        self.bookTitle = 'Learning python'
        self.categoryName = 'Python'
        self.createCategory =  Category.objects.create(name=self.categoryName)
        self.createBook = Book.objects.create(title=self.bookTitle, category=self.createCategory)

    def TestCategoryModelIsCreated(self):
        """Test that category model is created """
        initial_count = Category.objects.count()
        createCategory = Category.objects.create(name='New category')
        after_count = Category.objects.count()
        self.assertEquals(after_count, initial_count + 1)

    def TestCategoryNameIsUnique(self):
        """Test category name is unique """
        with self.assertRaise(IntegrityError):
            new_category = Category.objects.create(name=self.categoryName)

    def TestBookModelIsCreated(self):
        """Test that book model is created """
        initial_count = Book.objects.count()
        createBook = Book.objects.create(title="python basics", category= self.createCategory)    
