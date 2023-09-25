# Generated by Django 4.1.7 on 2023-09-23 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_alter_document_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='slug',
            field=models.SlugField(max_length=32, unique_for_date='dateCreate', verbose_name='Метка'),
        ),
    ]
