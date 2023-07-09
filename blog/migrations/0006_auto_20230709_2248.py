# Generated by Django 3.2.9 on 2023-07-09 14:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20211130_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reader', models.CharField(max_length=200)),
                ('comment_text', models.TextField()),
                ('agreed_numbers', models.IntegerField(default=0)),
                ('disgust_numbers', models.IntegerField(default=0)),
                ('approved_comment', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post')),
            ],
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]