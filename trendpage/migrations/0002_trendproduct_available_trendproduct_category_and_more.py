# Generated by Django 4.0.3 on 2022-03-05 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trendpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trendproduct',
            name='available',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='trendproduct',
            name='category',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='trendproduct',
            name='color',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='trendproduct',
            name='shipping',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='trendproduct',
            name='shipping_area',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]