# Generated by Django 4.1.2 on 2022-10-21 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0008_remove_issue_composer_spotlight_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='Summary',
            new_name='summary',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='first_impressions_body',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='first_impressions_desc',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='first_impressions_title',
        ),
        migrations.CreateModel(
            name='FirstImpressions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('desc', models.CharField(max_length=200, null=True)),
                ('body', models.TextField(blank=True)),
                ('first_impressions', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='newsletter.issue')),
            ],
        ),
    ]
