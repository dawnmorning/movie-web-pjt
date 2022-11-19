# Generated by Django 3.2 on 2022-11-18 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('communities', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='user',
            new_name='author',
        ),
        migrations.AddField(
            model_name='review',
            name='profile',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='author_profile', to='accounts.profile'),
            preserve_default=False,
        ),
    ]