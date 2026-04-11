from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('list_books/', views.list_books, name='list_books'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('<int:bookId>/', views.viewbook, name='view_one_book'),
    path('html5/links/', views.links, name='html5_links'),
    path('html5/text/formatting/', views.formatting, name='html5_formatting'),
    path('html5/listing/', views.listing, name='html5_listing'),
    path('html5/tables/', views.tables, name='html5_tables'),
    path('search/', views.search, name='books.search'),
    path('simple/query/', views.simple_query),
    path('complex/query/', views.lookup_query),
]