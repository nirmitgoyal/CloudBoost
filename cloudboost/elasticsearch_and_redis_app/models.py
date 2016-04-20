from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
@python_2_unicode_compatible


class Books(models.Model):
    # book_id = models.IntegerField()
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.name
