# Generated by Django 2.2.10 on 2021-10-01 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mydiary', '0007_newentry_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newentry',
            name='Author',
        ),
        migrations.AddField(
            model_name='newentry',
            name='username',
            field=models.CharField(default='admin', max_length=36),
        ),
    ]