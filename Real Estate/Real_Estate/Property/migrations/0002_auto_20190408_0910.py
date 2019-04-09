# Generated by Django 2.2 on 2019-04-08 09:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Property', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='properties',
            name='property_image',
        ),
        migrations.AddField(
            model_name='properties',
            name='property_image1',
            field=models.ImageField(default='property/default_property.jpg', upload_to='media/property'),
        ),
        migrations.AddField(
            model_name='properties',
            name='property_image5',
            field=models.ImageField(blank=True, default='property/default_property.jpg', upload_to='media/property'),
        ),
        migrations.AlterField(
            model_name='properties',
            name='property_image2',
            field=models.ImageField(blank=True, default='property/default_property.jpg', upload_to='media/property'),
        ),
        migrations.AlterField(
            model_name='properties',
            name='property_image3',
            field=models.ImageField(blank=True, default='property/default_property.jpg', upload_to='media/property'),
        ),
        migrations.AlterField(
            model_name='properties',
            name='property_image4',
            field=models.ImageField(blank=True, default='property/default_property.jpg', upload_to='media/property'),
        ),
    ]
