# Generated by Django 3.2.7 on 2021-09-02 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210902_0225'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='order_no',
            field=models.CharField(default='OrderNo: 12312', max_length=100),
        ),
    ]
