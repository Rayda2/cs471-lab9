from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Publisher
from django.db.models import Q, Count, Sum, Avg, Max, Min


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

def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def lookup_query(request):
    mybooks = Book.objects.filter(
        author__isnull=False
    ).filter(
        title__icontains='and'
    ).filter(
        edition__gte=2
    ).exclude(
        price__lte=100
    )[:10]

    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')




def task1(request):
    total = Book.objects.aggregate(total=Sum('quantity'))['total']

    books = Book.objects.all()

    for b in books:
        b.percent = (b.quantity / total) * 100 if total else 0

    return render(request, 'bookmodule/task1.html', {'books': books})

def task2(request):
    data = Publisher.objects.annotate(total=Sum('book__quantity'))
    return render(request, 'bookmodule/task2.html', {'data': data})

def task3(request):
    data = Publisher.objects.annotate(oldest=Min('book__pubdate'))
    return render(request, 'bookmodule/task3.html', {'data': data})

def task4(request):
    data = Publisher.objects.annotate(
        avg=Avg('book__price'),
        min=Min('book__price'),
        max=Max('book__price')
    )
    return render(request, 'bookmodule/task4.html', {'data': data})

def task5(request):
    data = Publisher.objects.annotate(
        high=Count('book', filter=Q(book__rating__gte=4))
    )
    return render(request, 'bookmodule/task5.html', {'data': data})

def task6(request):
    data = Publisher.objects.annotate(
        count=Count(
            'book',
            filter=Q(book__price__gt=50, book__quantity__lt=5, book__quantity__gte=1)
        )
    )
    return render(request, 'bookmodule/task6.html', {'data': data})