# Generated by Django 5.1.1 on 2024-09-29 07:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0012_note_audio_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notes.topic'),
        ),
    ]
