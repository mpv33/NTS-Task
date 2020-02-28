from django.db import models
class Client(models.Model):
    cid=models.CharField(max_length=10)
    fname = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    class Meta:
        db_table = "client"
