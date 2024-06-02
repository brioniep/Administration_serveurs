# Generated by Django 5.0.6 on 2024-06-02 12:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_applications', models.CharField(blank=True, max_length=100)),
                ('logo_utilisateur', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Serveurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_serveurs', models.CharField(max_length=100)),
                ('nombre_processeurs', models.IntegerField()),
                ('capacite_memoire', models.IntegerField()),
                ('capacite_stockage', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type_serveurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_srv', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_utilisateurs', models.CharField(max_length=100)),
                ('prenom', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_services', models.CharField(blank=True, max_length=100)),
                ('date_lancement', models.DateField()),
                ('espace_memoire_utilise', models.IntegerField(blank=True)),
                ('memoire_vive_necessaire', models.IntegerField()),
                ('serveur_de_lancement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monappli.serveurs')),
            ],
        ),
        migrations.CreateModel(
            name='Ressources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lien_applications', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monappli.applications')),
                ('lien_services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monappli.services')),
            ],
        ),
        migrations.AddField(
            model_name='serveurs',
            name='type_serveurs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monappli.type_serveurs'),
        ),
        migrations.AddField(
            model_name='applications',
            name='utilisateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monappli.utilisateurs'),
        ),
    ]