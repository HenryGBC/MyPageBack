# Generated by Django 2.0.4 on 2018-05-04 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
