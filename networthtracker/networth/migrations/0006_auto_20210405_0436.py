# Generated by Django 3.1.7 on 2021-04-05 04:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("networth", "0005_auto_20210404_2257")]

    operations = [
        migrations.RemoveField(model_name="account", name="account_number"),
        migrations.RemoveField(model_name="account", name="type"),
        migrations.AddField(
            model_name="account",
            name="description",
            field=models.CharField(max_length=300, null=True),
        ),
    ]
