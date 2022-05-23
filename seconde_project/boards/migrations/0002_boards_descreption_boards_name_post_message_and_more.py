# Generated by Django 4.0.3 on 2022-03-22 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boards',
            name='descreption',
            field=models.CharField(default=False, max_length=250),
        ),
        migrations.AddField(
            model_name='boards',
            name='name',
            field=models.CharField(default=True, max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='message',
            field=models.CharField(default=True, max_length=4000),
        ),
        migrations.AddField(
            model_name='post',
            name='posted_by',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='boards.topics'),
        ),
        migrations.AddField(
            model_name='topics',
            name='board',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='topic', to='boards.boards'),
        ),
        migrations.AddField(
            model_name='topics',
            name='creata_by',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='topic', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='topics',
            name='name',
            field=models.CharField(default=False, max_length=50, unique=True),
        ),
    ]