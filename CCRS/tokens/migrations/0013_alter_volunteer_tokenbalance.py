# Generated by Django 4.1.2 on 2022-11-04 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0012_alter_volunteerevent_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='tokenBalance',
            field=models.IntegerField(default=1),
        ),
    ]
