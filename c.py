from django.core.files import File
from os import listdir
from os.path import join
from json import loads
from Attributes.models import Author, Contributor, Language, Category, Book


DIR = "/opt/ebookify/books"

BOOKS = listdir(DIR)

for book in BOOKS:
	data = loads(open(join(DIR, book, "data.json"), "r").read())
	book = Book()
	title_and_subtitle = data["title"]
	if title_and_subtitle.count(":") > 0:
		book.title = title_and_subtitle.split(":")[0]
		book.subtitle = title_and_subtitle.split(":")[-1]
	else:
		book.title = title_and_subtitle
		book.subtitle = ""
	book.description = data["brief"]
	language = data["languages"][0].title()
	try:
		Language(name=language).save()
	except:
		pass
	book.language = Language.objects.get(name=language)
	authors = data["authors"]
	for i in range(len(authors)):
		authors[i] = authors[i].title()
		try:
			Author(full_name=authors[i], brief="").save()
		except:
			pass
	if len(authors) == 1:
		book.author1 = Author.objects.get(full_name=authors[0].title())
	elif len(authors) == 2:
		book.author1 = Author.objects.get(full_name=authors[0].title())
		book.author2 = Author.objects.get(full_name=authors[1].title())
	elif len(authors) == 3:
		book.author1 = Author.objects.get(full_name=authors[0].title())
		book.author2 = Author.objects.get(full_name=authors[1].title())
		book.author3 = Author.objects.get(full_name=authors[2].title())
	elif len(authors) == 4:
		book.author1 = Author.objects.get(full_name=authors[0].title())
		book.author2 = Author.objects.get(full_name=authors[1].title())
		book.author3 = Author.objects.get(full_name=authors[2].title())
		book.author4 = Author.objects.get(full_name=authors[3].title())
	elif len(authors) == 5:
		book.author1 = Author.objects.get(full_name=authors[0].title())
		book.author2 = Author.objects.get(full_name=authors[1].title())
		book.author3 = Author.objects.get(full_name=authors[2].title())
		book.author4 = Author.objects.get(full_name=authors[3].title())
		book.author5 = Author.objects.get(full_name=authors[4].title())
	contributors = data["contributors"]
	for i in range(len(contributors)):
		contributors[i] = contributors[i].title()
		try:
			Contributor(full_name=contributors[i]).save()
		except:
			pass
	if len(contributors) == 1:
		book.contributor1 = Contributor.objects.get(full_name=contributors[0])
	elif len(contributors) == 2:
		book.contributor1 = Contributor.objects.get(full_name=contributors[0])
		book.contributor2 = Contributor.objects.get(full_name=contributors[1])
	elif len(contributors) == 3:
		book.contributor1 = Contributor.objects.get(full_name=contributors[0])
		book.contributor2 = Contributor.objects.get(full_name=contributors[1])
		book.contributor3 = Contributor.objects.get(full_name=contributors[2])
	categories = data["categories"]
	for i in range(len(categories)):
		categories[i] = categories[i].title()
		try:
			Category(name=categories[i], brief="").save()
		except:
			pass
	if len(categories) == 1:
		book.category1 = Category.objects.get(name=categories[0])
	elif len(categories) == 2:
		book.category1 = Category.objects.get(name=categories[0])
		book.category2 = Category.objects.get(name=categories[1])
	elif len(categories) == 3:
		book.category1 = Category.objects.get(name=categories[0])
		book.category2 = Category.objects.get(name=categories[1])
		book.category3 = Category.objects.get(name=categories[2])
	elif len(categories) == 4:
		book.category1 = Category.objects.get(name=categories[0])
		book.category2 = Category.objects.get(name=categories[1])
		book.category3 = Category.objects.get(name=categories[2])
		book.category4 = Category.objects.get(name=categories[3])
	elif len(categories) == 5:
		book.category1 = Category.objects.get(name=categories[0])
		book.category2 = Category.objects.get(name=categories[1])
		book.category3 = Category.objects.get(name=categories[2])
		book.category4 = Category.objects.get(name=categories[3])
		book.category5 = Category.objects.get(name=categories[4])
	elif len(categories) == 6:
		book.category1 = Category.objects.get(name=categories[0])
		book.category2 = Category.objects.get(name=categories[1])
		book.category3 = Category.objects.get(name=categories[2])
		book.category4 = Category.objects.get(name=categories[3])
		book.category5 = Category.objects.get(name=categories[4])
		book.category6 = Category.objects.get(name=categories[5])
	elif len(categories) == 7:
		book.category1 = Category.objects.get(name=categories[0])
		book.category2 = Category.objects.get(name=categories[1])
		book.category3 = Category.objects.get(name=categories[2])
		book.category4 = Category.objects.get(name=categories[3])
		book.category5 = Category.objects.get(name=categories[4])
		book.category6 = Category.objects.get(name=categories[5])
		book.category7 = Category.objects.get(name=categories[6])
	elif len(categories) == 8:
		book.category1 = Category.objects.get(name=categories[0])
		book.category2 = Category.objects.get(name=categories[1])
		book.category3 = Category.objects.get(name=categories[2])
		book.category4 = Category.objects.get(name=categories[3])
		book.category5 = Category.objects.get(name=categories[4])
		book.category6 = Category.objects.get(name=categories[5])
		book.category7 = Category.objects.get(name=categories[6])
		book.category8 = Category.objects.get(name=categories[7])
	elif len(categories) == 9:
		book.category1 = Category.objects.get(name=categories[0])
		book.category2 = Category.objects.get(name=categories[1])
		book.category3 = Category.objects.get(name=categories[2])
		book.category4 = Category.objects.get(name=categories[3])
		book.category5 = Category.objects.get(name=categories[4])
		book.category6 = Category.objects.get(name=categories[5])
		book.category7 = Category.objects.get(name=categories[6])
		book.category8 = Category.objects.get(name=categories[7])
		book.category9 = Category.objects.get(name=categories[8])
	elif len(categories) >= 10:
		book.category1 = Category.objects.get(name=categories[0])
		book.category2 = Category.objects.get(name=categories[1])
		book.category3 = Category.objects.get(name=categories[2])
		book.category4 = Category.objects.get(name=categories[3])
		book.category5 = Category.objects.get(name=categories[4])
		book.category6 = Category.objects.get(name=categories[5])
		book.category7 = Category.objects.get(name=categories[6])
		book.category8 = Category.objects.get(name=categories[7])
		book.category9 = Category.objects.get(name=categories[8])
		book.category10 = Category.objects.get(name=categories[9])

	# adding files goes here
	# e.g.
	book.file1.save(str(book.identification), File(open("empty")))

	book.save()
