# Generated by Django 4.1.2 on 2022-11-03 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('name', models.CharField(max_length=100)),
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
                ('rewardCode', models.CharField(max_length=32, verbose_name='Reward Code')),
                ('expiryDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('name', models.CharField(max_length=100)),
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
                ('name', models.CharField(max_length=100)),
                ('userId', models.IntegerField(primary_key=True, serialize=False)),
                ('userEmail', models.CharField(max_length=200)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('tokenBalance', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Event Name')),
                ('date', models.DateTimeField()),
                ('description', models.TextField(blank=True)),
                ('confirmedVolunteers', models.ManyToManyField(blank=True, to='tokens.volunteer')),
                ('organiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tokens.organisation')),
            ],
        ),
    ]
