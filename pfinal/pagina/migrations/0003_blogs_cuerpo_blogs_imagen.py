# Generated by Django 4.2.2 on 2023-08-09 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0002_blogs_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='cuerpo',
            field=models.CharField(default=0, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogs',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='portada'),
        ),
    ]
