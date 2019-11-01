from django.db import models
from django.utils import timezone


class CommonInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        abstract = True


class Tag(CommonInfo):
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag


class Toast(CommonInfo):
    toast = models.TextField(max_length=500)
    tags = models.ManyToManyField(Tag, related_name="toasts")
    explicit = models.BooleanField(default=False, verbose_name="Explicit Language")
    disabled = models.BooleanField(default=False, verbose_name="Disabled")
    numUsed = models.IntegerField(default=0, verbose_name="Number of times used")

    def __str__(self):
        return self.toast
