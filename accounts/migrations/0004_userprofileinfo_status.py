# Generated by Django 3.0.5 on 2020-04-08 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200408_0439'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]