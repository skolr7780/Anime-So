# Generated by Django 3.2 on 2021-11-25 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_auto_20211126_0136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='season',
        ),
        migrations.RemoveField(
            model_name='season',
            name='serial',
        ),
        migrations.AddField(
            model_name='serial',
            name='episode',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Home.episode'),
        ),
        migrations.AddField(
            model_name='serial',
            name='season',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Home.season'),
        ),
    ]