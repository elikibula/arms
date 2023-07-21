# Generated by Django 4.2 on 2023-07-20 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arms', '0007_alter_armissue_arm_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armissue',
            name='arm_type',
            field=models.ForeignKey(blank=True, help_text='Do not enter, as it will be mapped to Serial Number', on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='arms.arm'),
        ),
        migrations.AlterField(
            model_name='armissue',
            name='serial_number',
            field=models.CharField(help_text='Please enter CORRECT serial number as it will show the Arm Type', max_length=200),
        ),
    ]
