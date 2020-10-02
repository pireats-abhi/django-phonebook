from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ContactList(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contactName = models.CharField(max_length=64)
    contactEmail = models.EmailField()
    contactNumber = models.IntegerField()