# Generated by Django 4.1.5 on 2023-02-06 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
