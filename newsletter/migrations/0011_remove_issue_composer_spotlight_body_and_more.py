# Generated by Django 4.1.2 on 2022-10-21 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0010_remove_firstimpressions_first_impressions_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='composer_spotlight_body',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='composer_spotlight_desc',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='composer_spotlight_title',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='never_gets_old_body',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='never_gets_old_desc',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='never_gets_old_title',
        ),
    ]
