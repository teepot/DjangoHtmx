from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import BookForm, AuthorForm, TagForm
from .models import Author, Book, Tag


def add_tag(request):

    tag_name = request.POST.get("tag_name")

    if tag_name:
        tag = Tag.objects.create(tag_name=tag_name)

    form = AuthorForm(request.POST)

    tag_form = TagForm()

    return render(
        request, "partials/author_form.html", {"form": form, "tag_form": tag_form}
    )


def create_author(request):

    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()

            return HttpResponse(f"Successfully saved {author.name}")

        else:
            return render(request, "partials/author_form.html", context={"form": form})

    form = AuthorForm()
    tag_form = TagForm()

    context = {"form": form, "tag_form": tag_form}

    return render(request, "create_author.html", context)


def create_book(request, pk):
    author = Author.objects.get(id=pk)
    books = Book.objects.filter(author=author)
    form = BookForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author
            book.save()
            return HttpResponse("success")
        else:
            return render(request, "partials/book_form.html", context={"form": form})

    context = {"form": form, "author": author, "books": books}

    return render(request, "create_book.html", context)


def create_book_form(request):
    form = BookForm()
    context = {"form": form}
    return render(request, "partials/book_form.html", context)
