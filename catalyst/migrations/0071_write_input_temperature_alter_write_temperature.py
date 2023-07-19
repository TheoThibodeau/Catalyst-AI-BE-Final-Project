# Generated by Django 4.2.3 on 2023-07-19 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst', '0070_alter_write_temperature'),
    ]

    operations = [
        migrations.AddField(
            model_name='write',
            name='input_temperature',
            field=models.FloatField(default=0.5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='write',
            name='temperature',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
