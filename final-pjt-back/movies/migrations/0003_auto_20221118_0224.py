# Generated by Django 3.2 on 2022-11-17 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20221117_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worldcuprecommend',
            name='genre_rank3',
        ),
        migrations.RemoveField(
            model_name='worldcuprecommend',
            name='genre_rank4',
        ),
        migrations.AlterField(
            model_name='worldcuprecommend',
            name='genre_rank1',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='worldcuprecommend',
            name='genre_rank2',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]