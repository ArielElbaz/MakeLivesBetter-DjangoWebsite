# Generated by Django 4.1 on 2022-09-02 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_userextend_store_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='stores',
            name='id_number',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]