# Generated by Django 4.1.7 on 2023-04-19 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_vnoplate_bookings_vid'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='userid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.registertable'),
        ),
    ]
