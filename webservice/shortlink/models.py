from django.db import models

# Create your models here.

class Link(models.Model):
     source_url = models.CharField(max_length=200, default='http://example.com', error_messages={'required': ''})
     short_url = models.CharField(max_length=15, default='sho.rt/link', error_messages={'required': ''})

     def __str__(self):
         return self.source_url

     def get_short_url(self):
         return self.short_url
