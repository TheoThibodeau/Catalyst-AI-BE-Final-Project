# Generated by Django 4.2.3 on 2023-07-19 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst', '0068_music_created_at_music_note_alter_music_concept_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='write',
            name='temperature',
            field=models.CharField(default=0.8),
        ),
    ]
