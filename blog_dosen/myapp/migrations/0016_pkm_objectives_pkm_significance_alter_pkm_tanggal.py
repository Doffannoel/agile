# Generated by Django 5.1.3 on 2025-02-26 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='pkm',
            name='objectives',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='pkm',
            name='significance',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='pkm',
            name='tanggal',
            field=models.DateField(default='2021-01-01'),
        ),
    ]
