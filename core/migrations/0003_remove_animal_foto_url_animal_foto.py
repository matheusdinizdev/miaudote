# Generated by Django 5.2.3 on 2025-06-14 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_customuser_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='foto_url',
        ),
        migrations.AddField(
            model_name='animal',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_pets/'),
        ),
    ]
