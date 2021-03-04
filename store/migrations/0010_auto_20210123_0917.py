# Generated by Django 3.1.5 on 2021-01-23 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20210123_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uom',
            name='height',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='uom',
            name='length',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='uom',
            name='quantity',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='uom',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='uom',
            name='width',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
