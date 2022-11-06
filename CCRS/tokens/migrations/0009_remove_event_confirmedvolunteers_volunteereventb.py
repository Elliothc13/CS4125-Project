# Generated by Django 4.1.2 on 2022-11-04 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0008_alter_volunteerevent_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='confirmedVolunteers',
        ),
        migrations.CreateModel(
            name='VolunteerEventB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('USER_APPLIED', 'User Applied'), ('USER_ADMITTED', 'User Admitted'), ('TOKENS_REQUESTED', 'Tokens Requested'), ('TOKENS_CLAIMED', 'Tokens Claimed')], default='USER_ADMITTED', max_length=50)),
                ('eventId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tokens.event')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tokens.volunteer')),
            ],
        ),
    ]