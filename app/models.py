import string
import random
from django.db import models

# Create your models here.
from django.utils import timezone


class Application(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False, blank=False)
    return_url = models.URLField(max_length=80, null=False, blank=False)
    created_date = models.DateTimeField(default=timezone.now, null=False, blank=False)
    application_secret = models.CharField(max_length=60, unique=True, blank=True)
    logo = models.ImageField(null=True, upload_to="static/logos")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.application_secret = ''.join(
                [random.choice(string.ascii_letters + string.digits) for n in range(60)])
        super(Application, self).save(args, kwargs)

    def __str__(self):
        return self.name
