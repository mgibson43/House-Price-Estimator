# Generated by Django 3.2.25 on 2024-05-12 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
