# Generated by Django 4.1 on 2022-08-31 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("open_food", "0003_alter_produto_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produto",
            name="code",
            field=models.IntegerField(max_length=20),
        ),
    ]
