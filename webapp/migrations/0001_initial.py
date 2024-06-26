# Generated by Django 5.0.4 on 2024-04-14 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('prenom', models.CharField(max_length=150)),
                ('nom', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=20)),
                ('adresse', models.CharField(max_length=500)),
                ('ville', models.CharField(max_length=150)),
                ('province', models.CharField(max_length=150)),
                ('pays', models.CharField(max_length=150)),
            ],
        ),
    ]
