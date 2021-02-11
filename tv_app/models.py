from django.db import models
import datetime

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 5 characters"
        if postData['title']:
            check_title = Show.objects.filter(title__contains=postData['title'])
            if len(check_title) > 0:
                errors["title"] = "The Show already exist"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 10 characters"
        if postData['release_date'] > str(datetime.datetime.now()):
            errors["release_date"] = "Release Date must be in the past"
        if not postData['release_date']:
            errors["release_date"] = "Input a valid Release Date"
        if 0 < len(postData['desc']) < 10:
            errors["desc"] = "Description is optional but should be at least 10 characters if you need it"

        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
