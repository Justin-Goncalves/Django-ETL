# Generated by Django 5.0.3 on 2024-04-24 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_alter_movie_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(choices=[(3, 'PG-13'), (2, 'PG'), (1, 'G'), (4, 'R'), (5, 'NC-17')]),
        ),
    ]