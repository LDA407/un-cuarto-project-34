# Generated by Django 4.1 on 2022-10-30 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('un_cuarto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutussection',
            name='thumbnails',
            field=models.ImageField(blank=True, default='img/img4.jpg', upload_to='img/about'),
        ),
    ]
