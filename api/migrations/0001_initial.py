# Generated by Django 3.2.12 on 2024-02-06 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dota2Teams',
            fields=[
                ('team_id', models.IntegerField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=100)),
                ('team_losses', models.IntegerField()),
                ('team_matches', models.IntegerField()),
                ('team_players', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Dota2Players',
            fields=[
                ('player_id', models.IntegerField(primary_key=True, serialize=False)),
                ('player_name', models.CharField(max_length=100)),
                ('player_position', models.CharField(max_length=100)),
                ('player_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dota2teams')),
            ],
        ),
    ]