# Generated by Django 5.1.5 on 2025-01-25 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_stocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stockname', models.CharField(max_length=100)),
                ('stockprice', models.IntegerField()),
                ('mrkcap', models.IntegerField()),
            ],
        ),
    ]
