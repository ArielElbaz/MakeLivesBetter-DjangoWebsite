# Generated by Django 4.1 on 2022-09-06 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0041_remove_userextend_approvals'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApprovedPost',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.post')),
                ('userExtend', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.userextend')),
            ],
            bases=('myapp.post',),
        ),
    ]
