# Generated by Django 5.2 on 2025-04-28 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='tipo',
            field=models.CharField(choices=[('interna', 'Interna'), ('externa', 'Externa')], default='interna', max_length=10),
        ),
        migrations.AddField(
            model_name='producto',
            name='marca',
            field=models.CharField(default='Sin marca', max_length=100),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, help_text='Imagen del producto', null=True, upload_to='productos/'),
        ),
    ]
