from django.db import models
class medicine(models.Model):
    tablet_name = models.CharField(max_length=250)
    e_date = models.DateTimeField()
    description = models.TextField()




    def __str__(self):
        return self.tablet_name
