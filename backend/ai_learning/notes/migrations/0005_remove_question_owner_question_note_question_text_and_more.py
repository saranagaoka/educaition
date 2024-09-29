# Generated by Django 5.1.1 on 2024-09-28 21:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_note_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='owner',
        ),
        migrations.AddField(
            model_name='question',
            name='note',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='notes.note'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.question')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
