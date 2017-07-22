from __future__ import unicode_literals

from django.db import models
#import re

#USERSNAME_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")


# Create your models here.
class UsersManager(models.Manager):
    def validate(self, form_data):

        errors = []

        if not len(form_data['usersname']) == len(form_data['usersname']):
            errors.append('Usersname already in use.')
        if not len(form_data['usersname']) >= 8 and len(form_data['usersname']) <=26:
                errors.append("Usersname not valid!")
                print "fuck you"
                #return redirect('/')
        else:
            errors.append("Usersname you entered is valid! Thank you")
            print "hell yea"
                #return errors(UsersManager, self).create(usersname=usersname)
        return errors
    def createUse(self, form_data):
        user = Users.objects.create(
        usersname = form_data['usersname']
        )
        return user


class Users(models.Model):
    usersname = models.CharField(max_length=1000)
    #email = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UsersManager()
