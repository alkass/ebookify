from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from pyqrcode import create as create_qrcode
from os.path import join
from Attributes.models import Author, Category, Book, BookFeedback

def homepage(request):
    authors = Author.objects.all().exclude(deprecated=True)
    categories = Category.objects.all().exclude(deprecated=True)
    books = Book.objects.all().exclude(deprecated=True)
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
    book = Book.objects.exclude(deprecated=True).filter(identification=identification)[0]
    feedbacks = BookFeedback.objects.filter(book=book).exclude(deprecated=True)
    book.authors = [
        book.author1,
        book.author2,
        book.author3,
        book.author4,
        book.author5
        ]
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
    return render(request, "view.html", locals())

def download(request, identification):
    return HttpResponse("this feature has not been implemented yet")
