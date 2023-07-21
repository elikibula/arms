# Generated by Django 4.2 on 2023-07-19 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arms', '0004_serialnumber_alter_armissue_id_alter_armtype_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armissue',
            name='serial_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arms.serialnumber'),
        ),
        migrations.AlterField(
            model_name='armtype',
            name='serial_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arms.serialnumber'),
        ),
    ]