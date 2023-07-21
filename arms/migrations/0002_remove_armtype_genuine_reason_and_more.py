# Generated by Django 4.2 on 2023-07-19 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='armtype',
            name='genuine_reason',
        ),
        migrations.AddField(
            model_name='armissue',
            name='genuine_reason',
            field=models.CharField(blank=True, choices=[('rfmf_personnel', 'RFMF Personnel'), ('navy_personnel', 'Navy Personnel'), ('police_personnel', 'Police Personnel'), ('civillian_personnel', 'Civillian Personnel')], max_length=200),
        ),
    ]