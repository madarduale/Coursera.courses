
from django.urls import path
from .views import index, upload, update_book, delete_book
urlpatterns = [
    path('home/', index, name="home"),
    path('upload/', upload, name = 'upload'),
    path('update/<int:book_id>/update/', update_book, name="upload-book"),
    path('delete/<int:book_id>/delete/', delete_book, name="delete-book")
]