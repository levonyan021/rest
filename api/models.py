from django.db import models

class Dota2Teams(models.Model):
    team_name = models.CharField(max_length=100)
    team_logo = models.ImageField(upload_to='images/', null=True, blank=True)
    team_losses = models.IntegerField()
    team_matches = models.IntegerField()
    team_players = models.IntegerField()

    def __str__(self):
        return self.team_name


class Dota2Players(models.Model):
    player_name = models.CharField(max_length=100)
    player_lastname = models.CharField(max_length=100)
    player_nickname = models.CharField(max_length=100)
    player_age = models.IntegerField()
    player_avatar = models.ImageField(upload_to='images/')
    player_team = models.ForeignKey(Dota2Teams, on_delete=models.CASCADE)
    player_position = models.CharField(max_length=100)
    player_rating = models.CharField(max_length=100)
    def __str__(self):
        return self.player_name

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.first_name