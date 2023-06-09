# Generated by Django 4.0.3 on 2022-12-23 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gitlab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gitlab',
            name='role',
            field=models.IntegerField(choices=[(5, 'minimal access'), (10, 'guest'), (20, 'reporter'), (30, 'developer'), (40, 'maintainer'), (50, 'owner')], default=5),
        ),
    ]
