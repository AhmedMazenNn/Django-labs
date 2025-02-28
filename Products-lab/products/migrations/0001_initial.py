# Generated by Django 5.1.6 on 2025-02-28 15:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('tags', models.TextField()),
                ('category', models.CharField(choices=[('Beauty', 'beauty'), ('technology', 'technology'), ('Health', 'health'), ('Groceries', 'groceries')], max_length=200)),
                ('thumbnail', models.URLField()),
            ],
        ),
    ]
