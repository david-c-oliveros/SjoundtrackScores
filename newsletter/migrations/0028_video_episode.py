# Generated by Django 4.1.2 on 2022-11-17 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0027_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='episode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='newsletter.episode'),
        ),
    ]