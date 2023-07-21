# Generated by Django 4.2 on 2023-07-19 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arms', '0006_arm_remove_armtype_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armissue',
            name='arm_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='arms.arm'),
        ),
    ]