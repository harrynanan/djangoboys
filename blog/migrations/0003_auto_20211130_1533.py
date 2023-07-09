# Generated by Django 3.2.9 on 2021-11-30 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211124_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='updated_date',
        ),
        migrations.AddField(
            model_name='comments',
            name='agreed_numbers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='disgust_numbers',
            field=models.IntegerField(default=0),
        ),
    ]
