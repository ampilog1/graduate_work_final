from django.db import models
from accounts.models import DearUser


class send_to_santa(models.Model):
    """ """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(
        auto_now_add=True)
    owner = models.ForeignKey(DearUser,
                              on_delete=models.CASCADE)


def __str__(self):
    return self.text


