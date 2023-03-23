from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = "__all__"

    def create(self, validated_data):
        authors_data = validated_data.pop("authors")
        book = Book.objects.create(**validated_data)
        for author_data in authors_data:
            author, _ = Author.objects.get_or_create(name=author_data["name"])
            book.authors.add(author)
        return book

    def update(self, instance, validated_data):
        authors_data = validated_data.pop("authors")
        instance.title = validated_data.get("title", instance.title)
        instance.publication_date = validated_data.get(
            "publication_date", instance.publication_date
        )
        instance.authors.clear()
        for author_data in authors_data:
            author, created = Author.objects.get_or_create(
                name=author_data["name"], email=author_data["email"]
            )
            instance.authors.add(author)
        instance.save()
        return instance
