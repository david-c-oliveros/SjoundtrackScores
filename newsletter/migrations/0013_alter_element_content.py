# Generated by Django 4.1.2 on 2022-10-22 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0012_element_remove_issue_first_impressions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
