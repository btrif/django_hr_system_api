# Generated by Django 4.0.5 on 2022-06-03 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64)),
                ('gender', models.CharField(max_length=1)),
                ('date_of_birth', models.DateField()),
                ('industry', models.CharField(max_length=64)),
                ('salary', models.FloatField(max_length=16)),
                ('years_of_experience', models.IntegerField(max_length=2)),
            ],
        ),
    ]
