# Generated by Django 2.0.2 on 2018-04-13 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capdb', '0033_auto_20180409_2117'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='casemetadata',
            index=models.Index(fields=['jurisdiction_id', 'decision_date', 'id'], name='capdb_casem_jurisdi_d41ebf_idx'),
        ),
    ]
