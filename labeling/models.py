from django.db import models
from accounts.models import User

class Article(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    pmid = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    pub_year = models.IntegerField()
    source = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    pubtype = models.CharField(max_length=200)

# Create your models here.
class Condition(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)

class Treatment(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200)  # medication, procedure
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

class CommonTreatmentAnnotation(models.Model):
    annotator = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    verifiers = models.ManyToManyField(User, related_name='g_verifiers')
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    treatments = models.ManyToManyField(Treatment, related_name='g_treatments')

class ConditionMeta(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)

    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    article_pool = models.ManyToManyField(Article, related_name='pool')
    marked_relevant = models.ManyToManyField(Article, related_name='cm_relevant')
    marked_irrelevant = models.ManyToManyField(Article, related_name='cm_irrelevant')
    contributors = models.ManyToManyField(User, related_name='cm_contributors')

class DemographicEntity(models.Model):
    title = models.CharField(max_length=200)
    subtype = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

class ContextualEntity(models.Model):
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

class RecommendationAnnotation(models.Model):
    is_recommended = models.BooleanField(default=True)

    annotator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='s_annotator')
    primary_condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    demographic_entities = models.ManyToManyField(DemographicEntity, related_name='s_demographics')
    contextual_entities = models.ManyToManyField(ContextualEntity, related_name='s_contexts')
    treatment_entities = models.ManyToManyField(Treatment, related_name='s_treatments')

    verifiers = models.ManyToManyField(User, related_name='s_verifiers')

class GeneralPopulationSummary(models.Model):
    associated_annotations = models.ManyToManyField(CommonTreatmentAnnotation, related_name='g_annotations')
    summarizer = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    primary_condition = models.ForeignKey(Condition, on_delete=models.CASCADE)

class SubpopulationSummary(models.Model):
    associated_annotations = models.ManyToManyField(RecommendationAnnotation, related_name='s_annotations')
    summarizer = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    primary_condition = models.ForeignKey(Condition, on_delete=models.CASCADE)