# Generated by Django 3.2.7 on 2021-09-02 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210902_0428'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='content',
            field=models.TextField(default='abc'),
            preserve_default=False,
        ),
    ]
