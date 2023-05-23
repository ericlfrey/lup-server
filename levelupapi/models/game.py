from django.db import models


class Game(models.Model):

    gamer = models.ForeignKey(
        "Gamer", on_delete=models.CASCADE, related_name='games')
    game_type = models.ForeignKey(
        "GameType", on_delete=models.CASCADE, related_name='games')
    maker = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()
