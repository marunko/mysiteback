# Generated by Django 5.1.4 on 2025-02-27 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_aboutme_summary_projects_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
    ]
