# Generated by Django 4.0.3 on 2022-04-21 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0004_child_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='imageUrl',
            field=models.TextField(null=True),
        ),
    ]