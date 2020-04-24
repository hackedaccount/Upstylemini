# Generated by Django 3.0.5 on 2020-04-24 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20200420_2145'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductsKeepa',
        ),
        migrations.RemoveField(
            model_name='products',
            name='id',
        ),
        migrations.AlterField(
            model_name='products',
            name='asin',
            field=models.CharField(max_length=500, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Category'),
        ),
    ]