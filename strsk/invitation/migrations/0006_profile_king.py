# Generated by Django 2.1 on 2019-08-10 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0005_profile_queen'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='king',
            field=models.CharField(default='King', max_length=50),
        ),
    ]
