# Generated by Django 4.1.2 on 2022-10-20 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0006_composerspotlight_firstimpressions_nevergetsold_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='first_impressions_michael_body',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='first_impressions_michael_desc',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='first_impressions_michael_title',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='first_impressions_robert_body',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='first_impressions_robert_desc',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='first_impressions_robert_title',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='first_impressions_stephen_body',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='first_impressions_stephen_desc',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='first_impressions_stephen_title',
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
        migrations.AddField(
            model_name='issue',
            name='composer_spotlight',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='newsletter.composerspotlight'),
        ),
        migrations.AddField(
            model_name='issue',
            name='first_impressions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='newsletter.firstimpressions'),
        ),
        migrations.AddField(
            model_name='issue',
            name='never_gets_old',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='newsletter.nevergetsold'),
        ),
        migrations.AddField(
            model_name='issue',
            name='summary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='newsletter.summary'),
        ),
    ]
