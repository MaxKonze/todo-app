# Generated by Django 5.0.6 on 2024-07-08 18:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("to_do", "0003_alter_todoitem_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todoitem",
            name="time",
            field=models.TimeField(default=0, max_length=11),
        ),
    ]
