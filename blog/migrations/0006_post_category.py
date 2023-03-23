# Generated by Django 4.1.7 on 2023-03-23 00:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0005_alter_post_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.CharField(
                choices=[("t", "Tutorial"), ("o", "Other")], default="o", max_length=1
            ),
        ),
    ]