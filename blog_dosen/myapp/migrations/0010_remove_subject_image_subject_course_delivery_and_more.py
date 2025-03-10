# Generated by Django 5.1.1 on 2025-02-23 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_subject_delete_learningoutcome_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='image',
        ),
        migrations.AddField(
            model_name='subject',
            name='course_delivery',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='course_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='cpl_table',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='forms_of_learning',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='learning_methods',
            field=models.TextField(blank=True, null=True),
        ),
    ]
