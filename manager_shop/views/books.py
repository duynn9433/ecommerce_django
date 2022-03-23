from django.shortcuts import render, redirect

# Create your views here.
from manager_shop.forms.books import AddBook, AddAuthor, AddPublisher
from manager_shop.models import Book, Author, Publisher


def book_index(request):
    books = Book.objects.all()
    authors = []
    links = []
    for b in books:
        authors.append(b.print_authors())
        links.append(str(b.id) + '/change')

    return render(request, 'books/index.html', {'books': books, 'authors': authors, 'links': links})


def author_index(request):
    authors = Author.objects.all()
    links = []
    for a in authors:
        links.append(str(a.id)+'/change')

    return render(request, 'books/author_index.html', {'authors': authors, 'links': links})


def publisher_index(request):
    pubs = Publisher.objects.all()
    links = []
    for a in pubs:
        links.append(str(a.id)+'/change')

    return render(request, 'books/publisher_index.html', {'pubs': pubs, 'links': links})


def book_change(request, id = None):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = AddBook(request.POST, instance=book)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            form.save_m2m()

            return redirect('/book/')

    add_book = AddBook(instance=book)
    return render(request, 'books/add.html', {'form': add_book})


def change_author(request, id = None):
    author = Author.objects.get(id=id)
    if request.method == 'POST':
        form = AddAuthor(request.POST, instance=author)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            form.save_m2m()
            return redirect('/book/author')

            # home = request.POST.get('home', '/')
            # return HttpResponseRedirect(home)  # Redirect after POST

    add_form = AddAuthor(instance=author)
    return render(request, 'books/add.html', {'form': add_form})


def change_publisher(request, id = None):
    pub = Publisher.objects.get(id=id)
    if request.method == 'POST':
        form = AddPublisher(request.POST, instance=pub)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            form.save_m2m()
            return redirect('/book/publisher')

            # home = request.POST.get('home', '/')
            # return HttpResponseRedirect(home)  # Redirect after POST

    add_form = AddPublisher(instance=pub)
    return render(request, 'books/add.html', {'form': add_form})


def book_add(request):
    if request.method == 'POST':
        form = AddBook(request.POST)
        if form.is_valid():
            form.save()
            # home = request.POST.get('home', '/')
            # return HttpResponseRedirect(home)  # Redirect after POST
            return redirect('/book')

    add_book = AddBook()
    return render(request, 'books/add.html', {'form': add_book})


def add_author(request):
    if request.method == 'POST':
        form = AddAuthor(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/book/author')

    add_author_form = AddAuthor()
    return render(request, 'books/add.html', {'form': add_author_form})


def add_publisher(request):
    if request.method == 'POST':
        form = AddPublisher(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/book/publisher')

    add_form = AddPublisher()
    return render(request, 'books/add.html', {'form': add_form})





