# Generated by Django 4.1.5 on 2023-06-01 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myvideo',
            name='link',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]