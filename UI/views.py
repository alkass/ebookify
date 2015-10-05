from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.db.models import Q
from pyqrcode import create as create_qrcode
from os.path import join
from Attributes.models import Author, Category, Language, Book, BookFeedback
from Attributes.forms import CategoryForm
from random import randint
from re import sub

"""
    B E G I N N I N G   -  O F  -  S T R I P P E R  -  F U N C T I O N S
"""

def getAuthors(book):
    authors = [
        book.author1,
        book.author2,
        book.author3,
        book.author4,
        book.author5
        ]
    while authors.count(None) > 0:
        authors.remove(None)
    for i in range(len(authors)):
        authors[i].brief = authors[i].brief.split("\n")
    return set(authors)

def getContributors(book):
    contributors = [
        book.contributor1,
        book.contributor2,
        book.contributor3
    ]
    while contributors.count(None) > 0:
        contributors.remove(None)
    return set(contributors)

def getCategories(book):
    categories = [
        book.category1,
        book.category2,
        book.category3,
        book.category4,
        book.category5,
        book.category6,
        book.category7,
        book.category8,
        book.category9,
        book.category10
        ]
    while categories.count(None) > 0:
        categories.remove(None)
    for i in range(len(categories)):
        categories[i].brief = categories[i].brief.split("\n")
    return set(categories)

"""
    E N D   -  O F  -  S T R I P P E R  -  F U N C T I O N S
"""

def homepage(request):
    authors = Author.objects.all().exclude(discoverable=False)
    categories = Category.objects.all().exclude(discoverable=False)
    books = Book.objects.all().exclude(discoverable=False)
    return render(request, "home.html", locals())

def main_options(request):
    return render(request, "main_options.html", {})

def search_page(request):
    authors = Author.objects.all().exclude(discoverable=False)
    categories = Category.objects.all().exclude(discoverable=False)
    languages = Language.objects.all().exclude(discoverable=False)
    books = Book.objects.all().exclude(discoverable=False)
    return render(request, "search_page.html", locals())

def upload_page(request):
    form = CategoryForm()
    return render(request, "upload_page.html", {"form":form})

def request_page(request):
    return render(request, "request_page.html", {})

def qr(request, identification):
    qr_code_img = create_qrcode("%s/%s" % (settings.PUBLIC_HOST_ADDRESS, identification))
    qr_file_path = join(settings.STATICFILES_DIRS[0], "media", "qr_codes", "%s.png" % identification)
    qr_code_img.png(qr_file_path, scale=11, module_color=(68, 50, 102), background=(243, 235, 246))
    return HttpResponse(file(qr_file_path, "rb").read(), {"Content-type":"img/png"})

def initials(request, full_name):
    tokenized_name = full_name.title().strip().split(" ")
    _initials = None
    if len(tokenized_name) == 1:
        _initials = tokenized_name[0][0]
    else:
        _initials = "%s%s" % (tokenized_name[0][0], tokenized_name[-1][0])
    initials_file_path = join(settings.STATICFILES_DIRS[0], "media", "author_initials", "%s.png" % _initials)
    return HttpResponse(file(initials_file_path, "rb").read(), {"Content-type":"img/png"})

def query(request):
    args = request.GET
    author = args.get("author", "all").title()
    category = args.get("category", "all").title()
    language = args.get("language", "all").title()
    search_tokens = sub("[ \t]+", " ", args.get("title", "")).title().strip().split(" ")
    books = Book.objects.exclude(discoverable=False)
    if author.lower() != "all" and len(author) > 0:
        author = Author.objects.get(full_name=author)
        books = books.filter(
            Q(author1=author)
            | Q(author2=author)
            | Q(author3=author)
            | Q(author4=author)
            | Q(author5=author)
            )
    if category.lower() != "all" and len(category) > 0:
        category = Category.objects.get(name=category)
        books = books.filter(
        Q(category1=category)
        | Q(category2=category)
        | Q(category3=category)
        | Q(category4=category)
        | Q(category5=category)
        | Q(category6=category)
        | Q(category7=category)
        | Q(category8=category)
        | Q(category9=category)
        | Q(category10=category)
        )
    if language.lower() != "all" and len(language) > 0:
        language = Language.objects.get(name=language)
        books = books.filter(language=language)
    for token in search_tokens:
        books = books.filter(Q(title__contains=token) | Q(subtitle__contains=token))
    return render(request, "query.html", locals())

def view(request, identification):
    book = None
    try:
        book = Book.objects.get(identification=identification)
    except (ValueError, Book.DoesNotExist):
        error = "Invalid link."
        return render(request, "view.html", locals())
    if book.discoverable:
        book.num_views += 1
        book.save()
        feedbacks = BookFeedback.objects.filter(book=book).exclude(discoverable=False)
        for i in range(len(feedbacks)):
            feedbacks[i].feedback = feedbacks[i].feedback.split("\n")
        book.authors = getAuthors(book)
        book.contributors = getContributors(book)
        book.categories = getCategories(book)
        return render(request, "view.html", locals())
    else:
        error = "This book is inaccessable. Sorry for the inconvenience."
        return render(request, "view.html", locals())

def view_random(request):
    books = Book.objects.exclude(discoverable=False)
    if len(books) == 0:
        error = "ebookify is currently out of books. Sorry for the inconvenience."
        return render(request, "view.html", {"error":error})
    else:
        book = books[randint(0, len(books) - 1)]
        return view(request, book.identification)

def download(request, identification):
    return HttpResponse("this feature has not been implemented yet")
