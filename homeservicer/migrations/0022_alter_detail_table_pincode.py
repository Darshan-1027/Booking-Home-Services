# Generated by Django 4.2.3 on 2024-03-29 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeservicer', '0021_alter_detail_table_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail_table',
            name='pincode',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
    ]
