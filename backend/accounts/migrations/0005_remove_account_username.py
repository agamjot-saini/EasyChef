# Generated by Django 4.1.7 on 2023-03-07 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_account_avatar_alter_account_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='username',
        ),
    ]
