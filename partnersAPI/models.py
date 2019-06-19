from django.contrib.auth.models import User
from django.contrib.gis.db import models

class Partner(models.Model):
	tradingName = models.CharField(max_length=100, blank=False)
	ownerName = models.CharField(max_length=100, blank=False)
	document = models.CharField(max_length=100, blank=False, unique=True)
	coverageArea = models.MultiPolygonField(blank=False)
	address = models.PointField(blank=False)
	owner = models.ForeignKey(User,  related_name='partners', on_delete=models.CASCADE, blank=True, null=True)