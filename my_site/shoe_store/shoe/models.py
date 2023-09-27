from django.db import models

class Shoe(models.Model):
    category = models.CharField(max_length=200)
    img = models.CharField(max_length=500)
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.category)
