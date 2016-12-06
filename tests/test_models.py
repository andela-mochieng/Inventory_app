from django.test import TestCase
from search.models import Book, Category
from django.db.utils import IntegrityError

class TestSearchModels(TestCase):
    """ Test search models """

    def setUp(self):
        """Model test set up """
        self.bookTitle = 'Learning python'
        self.categoryName = 'Python'
        self.new_category = 'New category'
        self.createCategory =  Category.objects.create(name=self.categoryName)
        self.createBook = Book.objects.create(title=self.bookTitle, category=self.createCategory)
        self.savedCategory = Category.objects.filter(name=self.categoryName)

    def TestCategoryModelIsCreated(self):
        """Test that category model is created """
        initial_count = Category.objects.count()
        createCategory = Category.objects.create(name=self.new_category)
        after_count = Category.objects.count()
        self.assertEquals(after_count, initial_count + 1)
        self.assertEquals(self.new_category, str(createCategory))

    def TestCategoryNameIsUnique(self):
        """Test category name is unique """
        with self.assertRaises(IntegrityError):
            new_category = Category.objects.create(name=self.categoryName)

    def TestBookModelIsCreated(self):
        """Test that book model is created """
        initial_count = Book.objects.count()
        createBook = Book.objects.create(title="python basics", category= self.createCategory)
        after_count = Book.objects.count()
        self.assertEquals(after_count, initial_count + 1)

    def TestCategoryModelInstance(self):
        category = Category.objects.create(name='category')
        self.assertIsInstance(category, Category)
