# Generated by Django 4.0.4 on 2022-05-28 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_contentchoice_post_post_choice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_rate',
            field=models.IntegerField(default=0),
        ),
    ]
