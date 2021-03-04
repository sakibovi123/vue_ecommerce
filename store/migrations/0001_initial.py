# Generated by Django 3.1.5 on 2021-01-18 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.CharField(max_length=200)),
                ('brand_image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Bundle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('bundle_img', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.CharField(max_length=200)),
                ('cat_image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curr_sign', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=155, null=True)),
                ('email', models.CharField(max_length=155, null=True, unique=True)),
                ('password', models.CharField(max_length=155, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='OrderManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_pass', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_title', models.CharField(default='Pending', max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='ProductColors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cl_name', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multi_images', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSizes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_name', models.CharField(blank=True, choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('img', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='UOM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_title', models.CharField(max_length=50)),
                ('category_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=200)),
                ('product_main_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('price', models.IntegerField(default=0, null=True)),
                ('discount_price', models.IntegerField(blank=True, default=0, null=True)),
                ('discount_percentage', models.IntegerField(blank=True, default=0, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('stock', models.BooleanField()),
                ('SKU', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
                ('color', models.ManyToManyField(blank=True, to='store.ProductColors')),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.currency')),
                ('product_other_images', models.ManyToManyField(blank=True, to='store.ProductImages')),
                ('size', models.ManyToManyField(blank=True, to='store.ProductSizes')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, null=True)),
                ('invoice', models.CharField(blank=True, max_length=10, null=True)),
                ('phone', models.CharField(max_length=12, null=True)),
                ('address', models.CharField(max_length=150, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('f_name', models.CharField(max_length=100, null=True)),
                ('order_status', models.CharField(blank=True, choices=[('PENDING', 'PENDING'), ('PICKED', 'PICKED'), ('DELIVERED', 'DELIVERED')], default='PENDING', max_length=155, null=True)),
                ('total', models.IntegerField(default=0, null=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='city', to='store.city')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='store.customer')),
                ('method', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='method', to='store.deliverymethod')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='store.product')),
            ],
        ),
    ]
