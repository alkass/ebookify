from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.db.models import Q
from django.conf import settings
from os.path import join
from Attributes.models import Author, Contributor, Category, Language, Book
from Attributes.forms import CategoryForm, BookForm
from random import randint
from re import sub

def homepage(request):
    num_authors = len(Author.objects.all().exclude(discoverable=False))
    num_categories = len(Category.objects.all().exclude(discoverable=False))
    num_books = len(Book.objects.all().exclude(discoverable=False))
    return render(request, "home.html", locals())

def main_options(request):
    return render(request, "main_options.html", {})

def search_page(request):
    authors = Author.objects.all().exclude(discoverable=False).order_by("full_name")
    categories = Category.objects.all().exclude(discoverable=False).order_by("name")
    languages = Language.objects.all().exclude(discoverable=False).order_by("name")
    return render(request, "search.html", locals())

def cover(request, identification):
    cover_img_name = str(Book.objects.exclude(discoverable=False).get(identification=identification).cover).split("/")[-1]
    return HttpResponse(file(join(settings.DATABASE_COVER_DIR, cover_img_name), "rb").read(), {"Content-type":"img/png"})

def query(request):
    args = request.GET
    author = args.get("author", "all").title()
    contributor = args.get("contributor", "all").title()
    category = args.get("category", "all").title()
    language = args.get("language", "all").title()
    search_tokens = sub("[ \t]+", " ", args.get("title", "")).title().strip().split(" ")
    books = Book.objects.exclude(discoverable=False).order_by("-recommended")
    if author.lower() != "all" and len(author) > 0:
        author = Author.objects.get(full_name=author)
        books = books.filter(authors__full_name=author)
    if contributor.lower() != "all" and len(contributor) > 0:
        contributor = Contributor.objects.get(full_name=contributor)
        books = books.filter(contributors__full_name=contributor)
    if category.lower() != "all" and len(category) > 0:
        category = Category.objects.get(name=category)
        books = books.filter(categories__name=category)
    if language.lower() != "all" and len(language) > 0:
        language = Language.objects.get(name=language)
        books = books.filter(language=language)
    for token in search_tokens:
        books = books.filter(Q(title__contains=token) | Q(subtitle__contains=token))
    return render(request, "query.html", {"books":books})

def view(request, identification):
    try:
        book = Book.objects.get(identification=identification)
        if book.discoverable:
            book.num_views += 1
            book.save()
            return render(request, "view.html", locals())
        else:
            error = "This book is inaccessable. Sorry for the inconvenience."
            return render(request, "view.html", locals())
    except (ValueError, Book.DoesNotExist):
        error = "Invalid link."
        return render(request, "view.html", locals())

def lucky(request):
    books = Book.objects.exclude(discoverable=False)
    if len(books) == 0:
        error = "we're currently out of books."
        return render(request, "view.html", {"error":error})
    else:
        recommended_books = books.filter(recommended=True)
        if len(recommended_books) > 0:
            random_book = recommended_books[randint(0, len(recommended_books)-1)]
        else:
            random_book = books[randint(0, len(books)-1)]
    return redirect("/view/%s" % str(random_book.identification))

def download(request):
    try:
        identification = request.GET.get("identification")
        extention = request.GET.get("extention", "").lower()
        book = Book.objects.exclude(discoverable=False).get(identification=identification)
        book.num_downloads += 1
        book.save()
        response = HttpResponse()
        path_to_file = None
        if extention == "pdf":
            path_to_file = join(settings.DATABASE_BOOK_DIR, str(book.pdf_file).split("/")[-1])
            response["Content-type"] = "application/pdf"
            response["Content-Disposition"] = "attachment; filename=%s.pdf" % book.title.replace(" ", "_")
        elif extention == "epub":
            path_to_file = join(settings.DATABASE_BOOK_DIR, str(book.epub_file).split("/")[-1])
            response["Content-type"] = "application/epub"
            response["Content-Disposition"] = "attachment; filename=%s.epub" % book.title.replace(" ", "_")
        elif extention == "mobi":
            path_to_file = join(settings.DATABASE_BOOK_DIR, str(book.mobi_file).split("/")[-1])
            response["Content-type"] = "application/mobi"
            response["Content-Disposition"] = "attachment; filename=%s.mobi" % book.title.replace(" ", "_")
        response.write(open(path_to_file, "rb").read())
        return response
    except Book.DoesNotExist:
        return HttpResponse("'%s' is an invalid book id" % identification)
    except ValueError:
        return HttpResponse("Error")
