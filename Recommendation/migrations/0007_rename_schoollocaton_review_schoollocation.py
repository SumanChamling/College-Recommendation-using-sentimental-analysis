# Generated by Django 3.2.13 on 2022-04-28 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recommendation', '0006_auto_20220428_0950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='schoollocaton',
            new_name='schoollocation',
        ),
    ]
