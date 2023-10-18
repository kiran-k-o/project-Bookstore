from django.urls import path
from .import views
from .views import Booklist, BookDetailView, SearchResultsListView, BookCheckout, add_to_cart, cart, remove_from_cart,ProfileView,AboutUsView
from . import views

urlpatterns = [
    path("",Booklist.as_view(),name="booklist"),
    path("detail/<int:pk>/",BookDetailView.as_view(),name="details"),
    path("search/", SearchResultsListView.as_view(),name="search"),
    path("checkout/<int:pk>/",BookCheckout.as_view(),name="checkout"),
    path('cart/',cart,name = 'mycart'),
    path("add_to_cart/<int:book_id>/",add_to_cart,name="add_to_cart"),
    path("remove_from_cart/<int:book_id>/",remove_from_cart,name="remove_from_cart"),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('aboutus/', AboutUsView.as_view(), name='aboutus')
]

