# Generated by Django 3.2 on 2021-05-16 12:31

from django.db import migrations, models
import django.db.models.deletion
import film.models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0011_film_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='photo',
            field=models.ImageField(upload_to=film.models.photo_path),
        ),
        migrations.AlterField(
            model_name='film',
            name='actors',
            field=models.ManyToManyField(related_name='actors', to='film.Actor'),
        ),
        migrations.AlterField(
            model_name='film',
            name='age_rating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='film.agerating'),
        ),
        migrations.AlterField(
            model_name='film',
            name='country',
            field=models.ManyToManyField(related_name='country', to='film.Country'),
        ),
        migrations.AlterField(
            model_name='film',
            name='direc',
            field=models.ManyToManyField(related_name='directors', to='film.Actor'),
        ),
        migrations.AlterField(
            model_name='film',
            name='photo',
            field=models.ImageField(max_length=1000, upload_to=film.models.photo_film_path),
        ),
    ]
