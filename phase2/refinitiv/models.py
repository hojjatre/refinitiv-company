from django.db import models

class Refinitiv(models.Model):
    name = models.CharField(max_length=200)
    ESG_score = models.IntegerField(null=False, default=0)
    rank = models.CharField(max_length=200)
    environment = models.IntegerField(null=False, default=0)
    social = models.IntegerField(null=False, default=0)
    governance = models.IntegerField(null=False, default=0)
    company_ticker = models.CharField(max_length=200)