from django import forms
from .models import Book, Author, Tag


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'title',
            'number_of_pages'
        )


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = "__all__"


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = "__all__"
