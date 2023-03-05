from django.db import models

# Create your models here.
average_incidents = (
    ('Password Reset', 'Password Reset'),
    ('Help Request', 'Help Request')
)

class Log(models.Model):
    time_called = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    callback_number = models.CharField(max_length=13)
    category= models.CharField(max_length=250, choices=average_incidents)
    notes = models.TextField(null=True)

    def __str__(self):
        return self.name + ' ' + self.callback_number

