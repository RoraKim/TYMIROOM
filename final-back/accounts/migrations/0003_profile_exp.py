# Generated by Django 3.2.12 on 2022-05-25 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_life_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='exp',
            field=models.IntegerField(default=0),
        ),
    ]
