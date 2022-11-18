# Generated by Django 3.2 on 2022-11-17 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorldcupRecommend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_rank1', models.IntegerField(null=True)),
                ('genre_rank2', models.IntegerField(null=True)),
                ('genre_rank3', models.IntegerField(null=True)),
                ('genre_rank4', models.IntegerField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worldcup_recommend', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='worldcuplogic',
            name='user',
        ),
        migrations.DeleteModel(
            name='Worldcup',
        ),
        migrations.DeleteModel(
            name='WorldcupLogic',
        ),
    ]