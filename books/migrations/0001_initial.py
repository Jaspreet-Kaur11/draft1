# Generated by Django 4.2.2 on 2023-06-07 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('cover_image', models.ImageField(upload_to='book_covers/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('average_rating', models.FloatField(default=0.0)),
                ('categories', models.TextField()),
            ],
        ),
    ]