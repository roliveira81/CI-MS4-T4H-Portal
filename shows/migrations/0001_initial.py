# Generated by Django 3.2.6 on 2021-09-08 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=254)),
                ('venue', models.CharField(max_length=254)),
                ('tickets_url', models.URLField(blank=True, max_length=1024, null=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]