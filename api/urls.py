from django.urls import path

from api.views import AddBookView, ListView, DetailView, UpdateView, DeleteView

urlpatterns = [
    path('add-book/', AddBookView.as_view(), name='add-book'),
    path('list-view/', ListView.as_view(), name='list-view'),
    path('detail-view/<int:pk>/', DetailView.as_view(), name='detail-view'),
    path('update-view/<int:pk>/', UpdateView.as_view(), name='update-view'),
    path('delete-view/<int:pk>/', DeleteView.as_view(), name='delete-view'),
]