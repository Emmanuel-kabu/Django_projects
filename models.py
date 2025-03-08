from django.db import models

# Create your models here.
class Topic(models.Model):
    """ A topic to be addeed"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add= True)


    def __str__(self):
        """ Return string representation of the model"""
        return self.text


class Entry(models.Model):
    """ what you have learn about specific topic"""
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class meta:
        verbose_name_plural = 'entries'


    def __str__(self):
        """ return the string reprensation of the model""" 
        return self.text[:50] +  '....'   