"""DjangoHtmx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from books.views import create_book_form, create_author, add_tag
from myapp import views
from books import views as book_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("create-contact/", views.create_contact, name="create-contact"),
    path("contacts/", views.ContactList.as_view(), name="contact-list"),
    path("delete-contact/<int:pk>/", views.delete_contact, name="delete-contact"),
    path("create-book/<int:pk>/", book_views.create_book, name="create-book"),
    path("htmx/create-book-form/", create_book_form, name="create-book-form"),
    path("create-author/", create_author, name="create-author"),
    path("add-tag/", add_tag, name="add-tag"),
]
