# Generated by Django 3.2.16 on 2023-06-08 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='contnt',
            new_name='content',
        ),
    ]
