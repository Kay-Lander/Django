from __future__ import unicode_literals

from django.db import models

# Create your models here.
class users(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add ="True")
    updated_at = models.DateTimeField(auto_now ="True")

class messages(models.Model):
    user_id = models.ForeignKey(users, related_name = "messages")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add ="True")
    updated_at = models.DateTimeField(auto_now="True")

class comments(models.Model):
    message_id = models.ForeignKey(messages, related_name = "comments")
    user_id = models.ForeignKey(users, related_name = "comments")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add="True")
    updated_at = models.DateTimeField(auto_now="True")

