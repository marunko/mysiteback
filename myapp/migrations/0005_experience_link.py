# Generated by Django 5.1.4 on 2025-02-28 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_contacts'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
