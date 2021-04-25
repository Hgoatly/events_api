from django.db import models


class Event(models.Model):
	start_time = models.DateTimeField(null=False, blank=False)
	end_time = models.DateTimeField(null=False, blank=False)
	label = models.CharField(max_length=100, null=False, blank=False)
	category = models.CharField(max_length=100, null=False, blank=False)
	comments = models.CharField(max_length=500, null=True, blank=True)

	def __str__(self):
		return self.label

