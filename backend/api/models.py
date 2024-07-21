from django.db import models

class Support_Ticket(models.Model):
    email = models.EmailField()
    date = models.DateField()
    issue = models.TextField()

    def __str__(self):
        return self.email