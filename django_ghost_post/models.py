from django.db import models
from django.utils import timezone

# Create your models here.

class BoastRoast(models.Model):
    roast_boast = ((True, 'Boast'), (False, 'Roast'))
    choices = models.BooleanField(choices=roast_boast, default=True)
    user_post = models.CharField(max_length=280, default='')
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    timeposted = models.DateTimeField(default=timezone.now)

    @property
    def votes(self):
        return self.upvote - self.downvote
