# Generated by Django 4.1.7 on 2023-03-21 14:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0002_author_last_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="author",
            options={"verbose_name": "Автор", "verbose_name_plural": "Авторы"},
        ),
        migrations.AlterModelOptions(
            name="book",
            options={"verbose_name": "Книга", "verbose_name_plural": "Книги"},
        ),
        migrations.AlterField(
            model_name="author",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="publication_date",
            field=models.DateField(null=True),
        ),
    ]
