# Generated by Django 4.1.2 on 2022-10-27 15:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('userId', models.IntegerField(primary_key=True, serialize=False)),
                ('userEmail', models.CharField(max_length=200)),
                ('businessName', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rewardCode', models.CharField(max_length=32, validators=[django.core.validators.MinLengthValidator(32)], verbose_name='Reward Code')),
                ('expiryDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('userId', models.IntegerField(primary_key=True, serialize=False)),
                ('userEmail', models.CharField(max_length=200)),
                ('organisationName', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('userId', models.IntegerField(primary_key=True, serialize=False)),
                ('userEmail', models.CharField(max_length=200)),
                ('firstName', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('tokenBalance', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]