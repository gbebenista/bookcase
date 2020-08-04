from django.urls import path

from books import views
from books.views import ListBookView, CreationBookView, DeleteBookView, UpdateBookView, DetailBookView, BasketListView

urlpatterns = [
    path('', ListBookView.as_view(), name='bookslist'),
    path('addbook', CreationBookView.as_view(), name='addbook'),
    path('deletebook/<pk>', DeleteBookView.as_view(), name='deletebook'),
    path('updatebook/<pk>', UpdateBookView.as_view(), name='updatebook'),
    path('detailbook/<pk>', DetailBookView.as_view(), name='detailbook'),
    path('add_to_basket', views.send_to_basket, name='addtobasket'),
    path('basket/user:<pk>', BasketListView.as_view(), name='basketlist'),
    path("delete_from_basket", views.delete_from_basket, name='deletefrombasket')
]