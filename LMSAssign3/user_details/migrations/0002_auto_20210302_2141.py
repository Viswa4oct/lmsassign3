# Generated by Django 3.1.7 on 2021-03-02 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(),
        ),
    ]
