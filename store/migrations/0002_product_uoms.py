# Generated by Django 3.1.5 on 2021-01-22 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='uoms',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.uom'),
        ),
    ]