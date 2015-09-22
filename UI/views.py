from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from pyqrcode import create as create_qrcode
from PIL import Image, ImageDraw, ImageFont
from os.path import join
from Attributes.models import Author, Category, Book

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
    book_info = Book.objects.filter(identification=identification)
    return HttpResponse(book_info["language"])

def download(request, identification):
    return HttpResponse("this feature has not been implemented yet")
