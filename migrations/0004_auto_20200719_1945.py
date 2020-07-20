# Generated by Django 3.0.7 on 2020-07-19 17:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_expenses', '0003_auto_20200710_0033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myexpenses',
            name='image',
        ),
        migrations.RemoveField(
            model_name='myexpenses',
            name='title',
        ),
        migrations.AddField(
            model_name='myexpenses',
            name='attachment',
            field=models.FileField(default=' ', upload_to='my_expenses/receipts/'),
        ),
        migrations.AddField(
            model_name='myexpenses',
            name='country',
            field=models.CharField(default='España', max_length=30),
        ),
        migrations.AddField(
            model_name='myexpenses',
            name='expense_name',
            field=models.CharField(default='Expense Name', max_length=100),
        ),
        migrations.AddField(
            model_name='myexpenses',
            name='receipt_num',
            field=models.CharField(default='1', max_length=32),
        ),
        migrations.AddField(
            model_name='myexpenses',
            name='recepit_date',
            field=models.DateField(default=django.utils.timezone.now, max_length=10),
        ),
        migrations.AddField(
            model_name='myexpenses',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='myexpenses',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='myexpenses',
            name='vat_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='myexpenses',
            name='vat_perc',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='myexpenses',
            name='vendor_address',
            field=models.CharField(default='address', max_length=100),
        ),
        migrations.AddField(
            model_name='myexpenses',
            name='vendor_name',
            field=models.CharField(default='Vendor', max_length=100),
        ),
        migrations.AddField(
            model_name='myexpenses',
            name='vendor_vat',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='myexpenses',
            name='category',
            field=models.CharField(default='categroy', max_length=100),
        ),
        migrations.AlterField(
            model_name='myexpenses',
            name='description',
            field=models.CharField(default='Description', max_length=240),
        ),
    ]
