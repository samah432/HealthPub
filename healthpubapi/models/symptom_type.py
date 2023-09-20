from django.db import models


class SymptomType(models.Model):
    type = models.CharField(max_length=255, default="Default Symptom")
