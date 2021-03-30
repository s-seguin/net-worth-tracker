# Generated by Django 3.1.7 on 2021-03-29 02:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("networth", "0003_asset_type"),
    ]

    operations = [
        migrations.RenameField(
            model_name="account", old_name="user_id", new_name="user"
        ),
        migrations.RenameField(model_name="asset", old_name="user_id", new_name="user"),
        migrations.AddField(
            model_name="transaction",
            name="user",
            field=models.ForeignKey(
                default="306ddf6e-bcec-4eea-96cc-c2a19365e0a7",
                on_delete=django.db.models.deletion.CASCADE,
                to="users.user",
            ),
            preserve_default=False,
        ),
    ]
