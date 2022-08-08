from django.db import models
from django.http import request


class Faculty(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Recommendation_faculty'

