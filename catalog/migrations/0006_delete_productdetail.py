# Generated by Django 4.0.3 on 2022-04-13 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_productdetail_test'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductDetail',
        ),
    ]