from django.db import models

# Create your models here.


class Countries(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    capital = models.CharField(max_length=50, blank=False, default='')

    class Meta:
        ordering = ('id', )

    def __str__(self):
        return self.name


class Task(models.Model):
    STATES = (('to do', 'To Do'), ('in progress', 'In Progress'), ('done','Done'))
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=STATES, default='todo')

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=50)
    CATEGORY_CHOICES = (('Essentials', 'Essentials'), ('Electronics', 'Electronics'), ('Groceries','Groceries'))
    categories = models.CharField(max_length=54, choices=CATEGORY_CHOICES, default='Essentials')

    def __str__(self):
        return self.name