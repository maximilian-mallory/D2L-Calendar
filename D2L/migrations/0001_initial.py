# Generated by Django 5.0.3 on 2024-06-23 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
