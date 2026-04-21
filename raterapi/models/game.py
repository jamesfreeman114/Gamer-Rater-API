from django.db import models
from django.conf import settings

class Game(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    designer = models.CharField(max_length=200)
    year_released = models.IntegerField()
    num_players = models.IntegerField()
    estimated_time = models.IntegerField()
    age_recommendation = models.IntegerField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='games'
    )

    @property
    def average_rating(self):
        """Average rating calculated attribute for each game"""
        ratings = self.ratings.all()

        total_rating = 0
        for rating in ratings:
            total_rating += rating.rating

        if total_rating == 0:
            return 0
        else:
            avg_rating = total_rating / len(ratings)
            return avg_rating