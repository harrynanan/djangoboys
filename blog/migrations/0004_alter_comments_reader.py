# Generated by Django 3.2.9 on 2021-11-30 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20211130_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='reader',
            field=models.CharField(max_length=200),
        ),
    ]
