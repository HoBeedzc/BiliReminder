# Generated by Django 3.2 on 2021-06-11 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
