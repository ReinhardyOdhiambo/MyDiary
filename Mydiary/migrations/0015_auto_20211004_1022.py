# Generated by Django 2.2.10 on 2021-10-04 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mydiary', '0014_auto_20211002_1642'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AddField(
            model_name='socials',
            name='bio',
            field=models.TextField(default='hello', max_length=1000),
        ),
    ]
