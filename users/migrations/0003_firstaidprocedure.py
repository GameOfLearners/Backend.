# Generated by Django 3.0.7 on 2020-06-25 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstAidProcedure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=25)),
                ('category', models.CharField(blank=True, max_length=50)),
                ('text', models.CharField(blank=True, max_length=250)),
            ],
        ),
    ]
