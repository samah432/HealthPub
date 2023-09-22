"""View module for handling requests for customer data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from healthpubapi.models import Appointment, Customer, SymptomType


class AppointmentView(ViewSet):
    """Honey Rae API customers view"""

    def list(self, request):
        """Handle GET requests to get all customers

        Returns:
            Response -- JSON serialized list of customers
        """

        appointments = Appointment.objects.all()
        serialized = AppointmentSerializer(appointments, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single customer

        Returns:
            Response -- JSON serialized customer record
        """

        appointment = Appointment.objects.get(pk=pk)
        serialized = AppointmentSerializer(appointment, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)
    

    
    def create(self, request):


        appointment = Appointment.objects.create(
        customer=Customer.objects.get(user=request.auth.user),
        description=request.data["description"],
        symptom_type=SymptomType.objects.get(pk=request.data["symptom_type"]),
        date=request.data["date"],
        )

        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)
    



    def destroy(self, request, pk):
        appointment = Appointment.objects.get(pk=pk)
        appointment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    


    def update(self, request, pk):

        appointment = Appointment.objects.get(pk=pk)
        appointment.customer=Customer.objects.get(user=request.auth.user)
        appointment.description = request.data["description"]
        appointment.symptom_type=SymptomType.objects.get(pk=request.data["symptom_type"])
        appointment.date = request.data["date"]


        symptom_type = SymptomType.objects.get(pk=pk)
        appointment.symptom_type = symptom_type
        appointment.save()


        return Response(None, status=status.HTTP_204_NO_CONTENT)

        



class AppointmentSerializer(serializers.ModelSerializer):
    """JSON serializer for customers"""
    class Meta:
        model = Appointment
        fields = ('id', 'customer', 'employee', 'description', 'symptom_type', 'date')