# Generated by Django 4.0.3 on 2022-07-11 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgUploader', '0004_remove_images_height_remove_images_width'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='file',
            field=models.ImageField(upload_to='static/'),
        ),
    ]
