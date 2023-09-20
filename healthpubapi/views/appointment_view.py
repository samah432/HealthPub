"""View module for handling requests for customer data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from healthpubapi.models import Appointment


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


class AppointmentSerializer(serializers.ModelSerializer):
    """JSON serializer for customers"""
    class Meta:
        model = Appointment
        fields = ('id', 'customer', 'employee', 'description', 'symptom_type', 'date')