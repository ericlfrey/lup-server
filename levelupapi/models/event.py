from django.db import models
# from .gamer import Gamer


class Event(models.Model):

    organizer = models.ForeignKey(
        "Gamer", on_delete=models.CASCADE, related_name='organized_events')
    game = models.ForeignKey(
        "Game", on_delete=models.CASCADE, related_name='events')
    description = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField()
    # attendees = models.ManyToManyField(Gamer, related_name="events")

    # @property
    # def joined(self):
    #     """Custom Property"""
    #     return self.__joined

    # @joined.setter
    # def joined(self, value):
    #     self.__joined = value
