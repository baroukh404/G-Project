# Generated by Django 4.1.5 on 2023-01-14 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=255)),
                ('Lastname', models.CharField(max_length=255)),
                ('Phone', models.IntegerField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('Filiere', models.CharField(max_length=255)),
                ('Parcours', models.CharField(max_length=255)),
            ],
        ),
    ]
