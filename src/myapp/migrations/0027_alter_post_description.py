# Generated by Django 4.1 on 2022-09-03 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_alter_stores_id_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=224, null=True),
        ),
    ]