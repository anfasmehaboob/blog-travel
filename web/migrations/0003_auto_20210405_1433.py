# Generated by Django 3.1.7 on 2021-04-05 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20210331_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='web'),
        ),
    ]
