# Generated by Django 4.1.2 on 2022-11-03 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0004_remove_business_name_remove_organisation_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='businessName',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='organisation',
            old_name='organisationName',
            new_name='name',
        ),
    ]
