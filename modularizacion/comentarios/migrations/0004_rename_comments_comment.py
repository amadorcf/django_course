# Generated by Django 4.1.1 on 2022-09-30 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0003_alter_comments_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='comments',
            new_name='Comment',
        ),
    ]
