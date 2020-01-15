# Generated by Django 3.0 on 2020-01-13 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('roll_no', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('dob', models.DateTimeField()),
                ('user_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(default=' ', max_length=254)),
                ('password1', models.CharField(max_length=100)),
                ('password2', models.CharField(max_length=100)),
                ('otp', models.CharField(max_length=4)),
                ('user_status', models.CharField(max_length=10)),
            ],
        ),
    ]
