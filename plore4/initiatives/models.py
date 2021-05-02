from django.db import models
from accounts.models import User

class Entity(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=350)

class StandardFieldValue(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=350)

class StandardField(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=350)
    possible_values = models.ManyToManyField(StandardFieldValue)

class DataDefinition(models.Model):
    entity_definitions = models.ManyToManyField(Entity)
    standard_fields = models.ManyToManyField(StandardField)

# Create your models here.
class Initiative(models.Model):
    title = models.CharField(max_length=200)
    mission_description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    publish_date = models.DateTimeField(auto_now_add=True, editable=False)
    # User Types
    contributors = models.ManyToManyField(User, related_name='contributors')
    managers = models.ManyToManyField(User, related_name='managers')

