# Generated by Django 4.1.5 on 2023-02-07 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='release_date',
            field=models.DateTimeField(null=True),
        ),
    ]
