# Generated by Django 4.0.3 on 2022-03-30 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='os',
            field=models.CharField(choices=[('windows', 'Windows'), ('linux', 'Linux'), ('mac_os', 'Mac Os')], default='linux', max_length=7),
            preserve_default=False,
        ),
    ]
