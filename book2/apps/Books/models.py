from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Authors(models.Model):
    name = models.CharField(max_length = 255)
    books_id = models.ForeignKey("Books", related_name = "authors")

class Books(models.Model):
    title = models.CharField(max_length = 255)
    publish_date = models.TextField()
    category = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    in_print = models.BooleanField()

    def __str__(self):
        output = "id: {}, title: {}, author: {}, publish_date: {}, category: {}, in_print: {}"
        return output.format(
            self.id,
            self.title,
            self.author,
            self.publish_date,
            self.category,
            self.in_print
        )






