from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
user = get_user_model()


class Hold(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)


class Visit(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)


class Sample(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)


