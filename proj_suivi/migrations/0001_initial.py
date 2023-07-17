# Generated by Django 4.2.3 on 2023-07-17 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collaborateurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poste', models.CharField(max_length=123)),
            ],
            options={
                'verbose_name': 'collaborateur',
            },
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=123)),
            ],
            options={
                'verbose_name': 'département',
            },
        ),
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=123)),
                ('commentaires', models.CharField(max_length=225)),
            ],
            options={
                'verbose_name': 'tache',
            },
        ),
        migrations.CreateModel(
            name='TacheCollaborateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collaborateur_id', models.ManyToManyField(to='proj_suivi.collaborateurs')),
                ('tache_id', models.ManyToManyField(to='proj_suivi.tache')),
            ],
            options={
                'verbose_name': 'tache_collab',
            },
        ),
        migrations.AddField(
            model_name='collaborateurs',
            name='departement_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proj_suivi.departement'),
        ),
        migrations.AddField(
            model_name='collaborateurs',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]