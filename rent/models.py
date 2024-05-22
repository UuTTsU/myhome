from django.db import models

class HomeRental(models.Model):
    title = models.CharField(default='saxli', max_length=500),
    address = models.CharField(max_length=500),
    description = models.TextField(),
    price = models.IntegerField(),
    available = models.BooleanField(),

    def __str__(self):
        return self.title
