# Generated by Django 2.1.2 on 2018-11-25 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('birthday', models.DateField(blank=True, default=None, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Actor',
                'verbose_name_plural': 'Actors',
            },
        ),
    ]