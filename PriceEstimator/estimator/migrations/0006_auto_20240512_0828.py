# Generated by Django 3.2.25 on 2024-05-12 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estimator', '0005_auto_20240512_0812'),
    ]

    operations = [
        migrations.RenameField(
            model_name='citycodes',
            old_name='city_id',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='citystate',
            old_name='state_id',
            new_name='state',
        ),
    ]