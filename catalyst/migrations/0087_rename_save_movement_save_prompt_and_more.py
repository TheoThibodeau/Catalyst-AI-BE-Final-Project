# Generated by Django 4.2.3 on 2023-07-23 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst', '0086_movement_save_music_save_visualart_save_write_save_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movement',
            old_name='save',
            new_name='save_prompt',
        ),
        migrations.RenameField(
            model_name='music',
            old_name='save',
            new_name='save_prompt',
        ),
        migrations.RenameField(
            model_name='visualart',
            old_name='save',
            new_name='save_prompt',
        ),
        migrations.RenameField(
            model_name='write',
            old_name='save',
            new_name='save_prompt',
        ),
    ]
