# Generated by Django 4.0.3 on 2022-03-22 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='tag',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
