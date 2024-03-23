# Generated by Django 3.2.25 on 2024-03-23 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price_confort', models.FloatField()),
                ('price_econ', models.FloatField()),
                ('city', models.CharField(max_length=50)),
                ('duration', models.IntegerField()),
                ('seat', models.CharField(max_length=5)),
                ('bed', models.CharField(max_length=5)),
            ],
        ),
    ]