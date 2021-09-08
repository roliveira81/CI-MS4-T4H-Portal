from django.db import models


class Show(models.Model):
    date = models.DateTimeField()
    location = models.CharField(max_length=254)
    venue = models.CharField(max_length=254)
    tickets_url = models.URLField(max_length=1024, null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.location
