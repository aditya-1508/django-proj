# Generated by Django 4.2.19 on 2025-02-28 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='connection',
            unique_together=set(),
        ),
    ]
