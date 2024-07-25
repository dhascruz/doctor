# Generated by Django 4.1.5 on 2024-07-25 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Cancelled', 'Cancelled')], default='Pending', max_length=10),
        ),
    ]
