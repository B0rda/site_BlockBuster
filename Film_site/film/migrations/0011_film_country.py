# Generated by Django 3.2 on 2021-05-14 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0010_film_trailer'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='country',
            field=models.ManyToManyField(blank=True, related_name='country', to='film.Country'),
        ),
    ]
