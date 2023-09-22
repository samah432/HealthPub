from django.db import models

class Appointment(models.Model):
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE, related_name='submitted_appointment')
    employee = models.ForeignKey("Employee", on_delete=models.CASCADE, related_name='assigned_employee', null=True, blank=True)
    description = models.CharField(max_length=400)
    symptom_type = models.ForeignKey("SymptomType", on_delete=models.CASCADE)
    date = models.DateField()


