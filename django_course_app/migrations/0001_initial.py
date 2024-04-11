# Generated by Django 5.0.4 on 2024-04-09 08:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailingAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_last_attempt', models.DateTimeField(null=True)),
                ('status_of_last_attempt', models.BooleanField(null=True)),
                ('server_response', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(null=True)),
                ('text', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(null=True)),
                ('interval', models.PositiveSmallIntegerField(choices=[(1, 'DAILY'), (2, 'WEEKLY'), (3, 'MONTHLY')], null=True)),
                ('mailing_status', models.PositiveSmallIntegerField(choices=[(1, 'CREATED'), (2, 'COMPLETED'), (3, 'LAUNCHED')], null=True)),
                ('message', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='django_course_app.message')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('comment', models.TextField(null=True)),
                ('newsletter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='django_course_app.newsletter')),
            ],
        ),
    ]
