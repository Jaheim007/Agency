# Generated by Django 4.0.5 on 2022-06-02 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.URLField()),
                ('rooms_number', models.IntegerField()),
                ('garage_number', models.IntegerField()),
                ('toillete_number', models.IntegerField()),
                ('address_name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=5)),
                ('longitude', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('delete_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_house', to='customers.customer')),
            ],
        ),
        migrations.CreateModel(
            name='HousePaymentPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('isactive', models.BooleanField(default=True)),
                ('description', models.TextField(null=True)),
                ('symbol', models.CharField(max_length=2)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('delete_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HouseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('isactive', models.BooleanField(default=True)),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('delete_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HouseImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('delete_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='house_houseimage', to='house.house')),
            ],
        ),
        migrations.AddField(
            model_name='house',
            name='house_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.housetype'),
        ),
        migrations.AddField(
            model_name='house',
            name='price_payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.housepaymentperiod'),
        ),
    ]
