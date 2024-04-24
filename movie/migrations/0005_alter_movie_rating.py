# Generated by Django 5.0.3 on 2024-03-18 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_alter_movie_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(choices=[(4, 'R'), (1, 'G'), (2, 'PG'), (5, 'NC-17'), (3, 'PG-13')]),
        ),
    ]