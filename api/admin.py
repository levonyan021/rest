from django.contrib import admin
from .models import Dota2Teams, Dota2Players, Person


@admin.register(Dota2Teams)
class Dota2TeamsAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'team_losses', 'team_matches', 'team_players')

@admin.register(Dota2Players)
class Dota2PlayersAdmin(admin.ModelAdmin):
    list_display = ('player_name', 'player_lastname', 'player_nickname', 'player_age', 'player_position', 'player_rating')

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')