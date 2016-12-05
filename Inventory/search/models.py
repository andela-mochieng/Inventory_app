from django.db import models

class Category(models.Model):
    """Create category model"""
    name = models.CharField(unique=True, max_length=250)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    """Creates book model"""
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __unicode__(self):
            return "{} in category {}".format(self.title, self.category)
