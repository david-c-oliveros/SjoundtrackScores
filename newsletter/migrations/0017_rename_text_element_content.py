# Generated by Django 4.1.2 on 2022-10-26 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0016_rename_content_element_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='element',
            old_name='text',
            new_name='content',
        ),
    ]
