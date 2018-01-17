from django.db import models


class Subscriber(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return "{} ({})".format(self.name, self.email)
