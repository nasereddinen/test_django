# Generated by Django 4.1.7 on 2023-04-06 06:07

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
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siret', models.CharField(max_length=50)),
                ('raison_sociale', models.CharField(max_length=50)),
                ('compte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dynef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix', models.FloatField()),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='EnergyCounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=50)),
                ('code_postal', models.CharField(max_length=50)),
                ('ville', models.CharField(max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voltocms.company')),
            ],
        ),
        migrations.CreateModel(
            name='TotalEnergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField()),
                ('prix', models.IntegerField()),
                ('date_fin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='EnergyHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('result', models.FloatField(blank=True, null=True)),
                ('compteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voltocms.energycounter')),
                ('dynef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voltocms.dynef')),
                ('total_energie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voltocms.totalenergy')),
            ],
        ),
    ]
