from django.db import models


class Drug(models.Model):
    # if not exist in text search create
    name = models.TextField()
    verified = models.BooleanField(default=False)
    


