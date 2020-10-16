# Generated by Django 3.1.2 on 2020-10-12 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('miles', models.FloatField()),
                ('elevationGain', models.FloatField()),
                ('elevationLoss', models.FloatField()),
                ('description', models.TextField()),
                ('starred', models.BooleanField()),
            ],
        ),
    ]