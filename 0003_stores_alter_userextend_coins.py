# Generated by Django 4.1 on 2022-08-27 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_feature_details_userextend'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('product', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='userextend',
            name='coins',
            field=models.IntegerField(),
        ),
    ]
