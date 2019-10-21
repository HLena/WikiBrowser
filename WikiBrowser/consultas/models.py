from django.db import models

# Create your models here.
class WebPages(models.Model):
    id_page = models.IntegerField()
    page_rank = models.FloatField()
    url = models.URLField(max_length=300)


class Words(models.Model):
    word = models.CharField(max_length = 50)
    id_page = models.ForeignKey(WebPages,on_delete=models.CASCADE)
