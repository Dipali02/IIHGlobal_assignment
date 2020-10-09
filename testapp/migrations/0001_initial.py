# Generated by Django 3.0.8 on 2020-10-09 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('dob', models.DateField(max_length=20, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
