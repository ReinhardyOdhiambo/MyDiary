# Generated by Django 2.2.10 on 2021-10-02 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mydiary', '0010_remove_socials_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(default='hello', max_length=1000),
        ),
    ]
