# Generated by Django 2.0.4 on 2018-04-21 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='description',
            field=models.CharField(default='Enter Something about your Movie Tastes and Background', max_length=1000),
        ),
    ]