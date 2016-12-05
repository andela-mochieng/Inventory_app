from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from search.models import Book, Category


class TestSearchViewFunctionality(TestCase):
    """Test search view functionality"""

    def setUp(self):
        self.client = client
        self.search_url = reverse('search')
        self.categoryName = 'Python'
        self.bookTitle = 'learning python basics'
        self.partialBookName = 'learning'
        self.caseinsensitiveBookName = 'LEARNING python basics'
        self.categorySearch = {'category': self.categoryName }
        self.bookSearch = {'querystring' : self.bookTitle }
        self.SearchBookInCategory = {'querystring': self.bookTitle, 'category': self.categoryName}
        self.SearchPartialbookTitle = {'querystring': self.partialbookTitle, 'category': self.categoryName}
        self.SearchcaseInsensitiveBookTitle = {'querystring': self.caseinsensitiveBookName, 'category': self.categoryName}
        self.unknownbooktitle = 'Javascript'
        self.emptySearch = {'querystring': '', 'category': ''}

        def TestSearchViewFunctionalityWorks(self):
            """Test search functionality works and returns the required data"""
            response = self.client.get(self.search_url, self.SearchBookInCategory)
            self.assertTrue(response.status_code, 200)
            self.assertIn(self.SearchBookInCategory, str(response.context[object_list][0]))

        def TestBookTitleSearchIsCaseInsensitive(self):
            """Test book title search is case insensitive"""
            response = self.client.get(self.search_url, self.SearchcaseInsensitiveBookTitle)
            self.assertTrue(response.status_code, 200)
            self.assertIn(self.SearchBookInCategory, str(response.context[object_list][0]))

        def TestPartialBookTitleSearchWorks(self):
            """Test user can search by partial book titles """
            response = self.client.get(self.search_url,self.SearchPartialbookTitle)
            self.assertTrue(response.status_code, 200)
            self.assertIn(self.SearchBookInCategory, str(response.context[object_list][0]))


        def Test404isRaisedThenSearchArgurmentsAreUnknown(self):
            """Test 404 is raised then book title doesnt exist """
            response = self.client.get(self.search_url, {'querystring':self.unknownbooktitle })
            self.assertTrue(response.status_code, 404)


        def TestSearchByCategoryOnlyIsSuccessful(self):
            """Test search by category only is successful"""
            response = self.client.get(self.search_url, self.categorySearch)
            self.assertTrue(response.status_code, 200)
            self.assertIn(self.categorySearch , str(response.context['object_list'][0]))


        def TestSearchByBooktitleOnlyIsSuccessful(self):
            """Test search by book title only is successful"""
            response = self.client.get(self.search_url, self.bookSearch)
            self.assertTrue(response.status_code, 200)
            self.assertIn(self.bookSearch, str(response.context['object_list'][0]))

        def TestEmptySearchArguments(self):
            """Test that an empty search argument returns all the books in the db """
            response = self.client.get(self.search_url, self.emptySearch)
            all_books = Book.objects.all()
            self.assertTrue(response.status_code, 200)
            self.assertIn(all_books, response..context['object_list'][0])
