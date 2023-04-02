# Generated by Django 4.0.5 on 2022-06-03 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_alter_employee_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='industry',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.FloatField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='years_of_experience',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
