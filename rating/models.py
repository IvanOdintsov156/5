from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Comic(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    rating = models.FloatField(default=0)

class Rating(models.Model):
    comic = models.ForeignKey(Comic, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
@receiver([post_save, post_delete], sender=Rating)
def update_comic_rating(sender, instance, **kwargs):
    comic = instance.comic
    ratings = comic.ratings.all()
    average_rating = ratings.aggregate(models.Avg('value'))['value__avg']
    comic.rating = average_rating if average_rating else 0
    comic.save(update_fields=['rating'])

    