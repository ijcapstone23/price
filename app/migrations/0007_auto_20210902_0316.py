# Generated by Django 3.2.7 on 2021-09-02 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210902_0229'),
    ]

    operations = [
        migrations.AddField(
            model_name='popup',
            name='target_url',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='popup',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='popup',
            name='photo',
            field=models.ImageField(upload_to='pop_up'),
        ),
        migrations.AlterField(
            model_name='popup',
            name='width',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
