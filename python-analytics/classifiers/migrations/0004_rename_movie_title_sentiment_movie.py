# Generated by Django 4.2.5 on 2023-09-24 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classifiers', '0003_rename_movie_sentiment_movie_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sentiment',
            old_name='movie_title',
            new_name='movie',
        ),
    ]