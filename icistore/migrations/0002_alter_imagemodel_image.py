# Generated by Django 4.2.6 on 2023-10-12 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icistore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='image',
            field=models.ImageField(upload_to='f"{timezone.now(year)}/{today.month:02d}/{today.day:02d}'),
        ),
    ]
