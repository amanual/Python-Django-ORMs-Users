from __future__ import unicode_literals

from django.db import models
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email_address = models.CharField(max_length = 255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    
#get all users
# get last user
# creat a few records in the users
# get first user
# get users sorted by their first name (order by first_name DESC)
# Get the record of the user whose id is 3 and UPDATE the person's last_name to something else. Know how to do this directly in the console using .get and .save.
# delete a record of a user whose id is 4 (use something like User.objects.get(id=2).delete...).
# (optional) Ninja:
# Find a way to validate the data coming in to the shell.  For example, make sure that "name" fields are a minimum length, "email" is a valid email, or that "email" doesn't already exist in the db.

    
