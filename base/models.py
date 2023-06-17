from django.db import models
from django.contrib.auth.models import User
class Task(models.Model):
    #many to one rel
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) #if we delete user we delete the data too
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete =models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)#automatic takes the date time and adds it

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']#ordering by complete status
