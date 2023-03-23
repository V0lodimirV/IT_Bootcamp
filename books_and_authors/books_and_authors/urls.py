"""books_and_authors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from books import views
from .yasg import urlpatterns as doc_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/authors/", views.authors),
    path("api/v1/authors/<int:author_id>/", views.author_detail),
    path("api/v1/books/", views.books),
    path("api/v1/books/<int:book_id>/", views.book_detail),
]

urlpatterns += doc_urls
