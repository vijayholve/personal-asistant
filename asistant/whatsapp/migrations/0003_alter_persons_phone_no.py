# Generated by Django 5.0.6 on 2024-06-12 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatsapp', '0002_alter_persons_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persons',
            name='phone_no',
            field=models.CharField(max_length=15),
        ),
    ]
