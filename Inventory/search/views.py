from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from django.http import Http404
from .models import Book, Category

class SearchListView(ListView):
    model = Book
    template_name = 'search/search.html'

    def get_context_data(self, **kwargs):
        """Override the SearchListView default context data """
        context = super(SearchListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        """ Implements the search functionality ie search by both title and category
        or by either title or category it raises 404 on an unknown search """
        querystring = self.request.GET.get('title', '')
        categoryName = self.request.GET.get('categoryName', '')
        search_results = ""
        if querystring and categoryName:
            search_results = Book.objects.filter(Q(category__name__iexact=categoryName) & Q(title__icontains=querystring))
        elif querystring:
            search_results = Book.objects.filter(title__icontains=querystring)
        elif categoryName:
            search_results = Book.objects.filter(category__name__iexact=categoryName)
        else:
            return Book.objects.all()
        if search_results:
            return search_results
        else:
            raise Http404('No search book title or Category exits')
