# Generated by Django 4.2.3 on 2023-08-22 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0003_blogs_cuerpo_blogs_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='cuerpo',
            field=models.CharField(max_length=1200),
        ),
    ]
