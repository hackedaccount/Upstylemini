# Generated by Django 3.0.5 on 2020-04-18 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20200418_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]