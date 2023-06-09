# Generated by Django 4.0.3 on 2022-03-25 07:07

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('employees', models.ManyToManyField(related_name='groups', to='employees.employee')),
                ('parent', mptt.fields.TreeForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='groups.group')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
