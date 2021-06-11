# Generated by Django 3.2 on 2021-06-11 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=20)),
                ('bili_uid', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=10)),
                ('pwd', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='User.user')),
            ],
        ),
    ]