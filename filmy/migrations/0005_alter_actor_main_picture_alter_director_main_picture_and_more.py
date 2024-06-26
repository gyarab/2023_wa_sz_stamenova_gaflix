# Generated by Django 5.0.6 on 2024-06-14 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0004_actor_director_movie_genres_movie_actors_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='main_picture',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='director',
            name='main_picture',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='movie',
            name='main_picture',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
    ]
