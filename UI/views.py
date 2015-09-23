from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from pyqrcode import create as create_qrcode
from os.path import join
from Attributes.models import Author, Category, Book, BookFeedback
from random import randint

def homepage(request):
    authors = Author.objects.all().exclude(discoverable=False)
    categories = Category.objects.all().exclude(discoverable=False)
    books = Book.objects.all().exclude(discoverable=False)
    return render(request, "home.html", locals())

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

def view(request, identification):
    book = Book.objects.exclude(discoverable=False).get(identification=identification)
    book.num_views += 1
    book.save()
    feedbacks = BookFeedback.objects.filter(book=book).exclude(discoverable=False)
    for i in range(len(feedbacks)):
        feedbacks[i].feedback = feedbacks[i].feedback.split("\n")
    book.authors = [
        book.author1,
        book.author2,
        book.author3,
        book.author4,
        book.author5
        ]
    while book.authors.count(None) > 0:
        book.authors.remove(None)
    for i in range(len(book.authors)):
        book.authors[i].brief = book.authors[i].brief.split("\n")
    book.authors = set(book.authors)
    book.categories = [
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
    while book.categories.count(None) > 0:
        book.categories.remove(None)
    for i in range(len(book.categories)):
        book.categories[i].brief = book.categories[i].brief.split("\n")
    book.categories = set(book.categories)
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
