# Generated by Django 4.2.3 on 2023-07-17 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proj_suivi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collaborateurs',
            name='user',
        ),
        migrations.AddField(
            model_name='collaborateurs',
            name='nom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nom', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='collaborateurs',
            name='prenom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prenom', to=settings.AUTH_USER_MODEL),
        ),
    ]
