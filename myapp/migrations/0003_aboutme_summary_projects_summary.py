# Generated by Django 5.1.4 on 2025-02-26 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_token_expires_at_alter_token_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='summary',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='summary',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
