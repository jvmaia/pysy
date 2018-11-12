from .serializers import State_serializer, Doctor_serializer, Doctor_id_serializer, Patient_serializer, Medical_appointment_id_serializer, Medical_appointment_serializer
from .models import Doctor, Patient, Medical_appointment, State

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StateList(APIView):
    """
    get:
        Return a list of states availables

    """

    def get(self, request, format=None):
        states = State.objects.all()
        serializer = State_serializer(states, many=True)
        return Response(serializer.data)


class DoctorList(APIView):
    """
    get:
        Return a list of doctors.

    post:
        Create a doctor instance.

    """

    def get(self, request, format=None):
        doctors = Doctor.objects.all().order_by('id')
        serializer = Doctor_id_serializer(doctors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Doctor_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorChanges(APIView):
    """
    delete:
        Delete a doctor instance.

    put:
        Change a doctor instance.
    """

    def delete(self, request, pk, format=None):
        doctor = Doctor.objects.get(pk=pk)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        doctor = Doctor.objects.get(pk=pk)
        serializer = Doctor_serializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientList(APIView):
    """
    get:
        Return a list of patients.

    post:
        Create a new patient instance.

    """

    def get(self, request, format=None):
        patients = Patient.objects.all()
        serializer = Patient_serializer(patients, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Patient_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientChanges(APIView):
    """
    delete:
        Delete a patient instance.

    put:
        Change a patient instance.
    """

    def delete(self, request, pk, format=None):
        patient = Patient.objects.get(pk=pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        patient = Patient.objects.get(pk=pk)
        serializer = Patient_serializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MedicalApp(APIView):
    """
    get:
        Return a list of specifical medical appointments based on doctor_id.

    delete:
        Delete a medical appointment instance.

    put:
        Change a medical appointment instance.

    """

    def get(self, request, pk, format=None):
        doctor = Doctor.objects.get(pk=pk)
        medical_apps = Medical_appointment.objects.filter(doctor=doctor)
        serializer = Medical_appointment_id_serializer(medical_apps, many=True)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        medical_app = Medical_appointment.objects.get(pk=pk)
        medical_app.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        medical_app = Medical_appointment.objects.get(pk=pk)
        serializer = Medical_appointment_id_serializer(
            medical_app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MedicalappsList(APIView):
    """
    get:
        Return a list of medical appointments.

    post:
        Create a new medical appointment instance.

    """

    def get(self, request, format=None):
        medical_apps = Medical_appointment.objects.all().order_by('-date')
        serializer = Medical_appointment_id_serializer(medical_apps, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Medical_appointment_serializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
