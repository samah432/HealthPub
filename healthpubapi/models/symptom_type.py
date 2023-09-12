from django.db import models


class SymptomType(models.Model):
    symptom_type = models.CharField(max_length=255)
