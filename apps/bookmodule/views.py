from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})


def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))


def list_books(request):
    return render(request, "bookmodule/list_books.html")


def viewbook(request, bookId):
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}

    targetBook = None

    if book1['id'] == bookId:
        targetBook = book1
    elif book2['id'] == bookId:
        targetBook = book2

    context = {'book': targetBook}

    return render(request, 'bookmodule/one_book.html', context)


def aboutus(request):
    return render(request, "bookmodule/aboutus.html")

def links(request):
    return render(request, 'bookmodule/html5/links.html')

def formatting(request):
    return render(request, 'bookmodule/html5/formatting.html')

def listing(request):
    return render(request, 'bookmodule/html5/listing.html')

def tables(request):
    return render(request, 'bookmodule/html5/tables.html')



def __getBooksList():
    return [
        {'id':1, 'title':'Continuous Delivery', 'author':'J.Humble'},
        {'id':2, 'title':'Reverse Engineering', 'author':'E. Eilam'},
        {'id':3, 'title':'Machine Learning Book', 'author':'Burkov'}
    ]

def search(request):

    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        newBooks = []

        for item in books:
            if isTitle and string in item['title'].lower():
                newBooks.append(item)
            elif isAuthor and string in item['author'].lower():
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})


    return render(request, 'bookmodule/search.html')