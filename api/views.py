from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from api.forms import BookForm
from api.models import Book

# Create your views here.

class AddBookView(CreateView):
    form_class = BookForm
    template_name = 'add_book.html'
    success_url = '/api/add-book/'


class ListView(ListView):
    model = Book
    template_name = 'list_view.html'
    success_url = '/api/list-view/'


class DetailView(DetailView):
    model = Book
    template_name = 'detail_view.html'
    success_url = '/api/detail-view/'


class UpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'update_view.html'
    def get_success_url(self):
        return reverse_lazy('update-view', kwargs={'pk': self.object.pk})
    

class DeleteView(DeleteView):
    model = Book
    template_name = 'delete_view.html'
    success_url = reverse_lazy('list-view')