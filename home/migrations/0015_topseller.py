# Generated by Django 4.2 on 2023-06-12 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topseller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('info', models.TextField()),
                ('date', models.DateField()),
                ('author', models.CharField(max_length=50)),
            ],
        ),
    ]