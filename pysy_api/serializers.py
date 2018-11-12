from .models import State, Doctor, Patient, Medical_appointment

from rest_framework import serializers


class State_serializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = '__all__'


class Doctor_serializer(serializers.ModelSerializer):
    photo = serializers.ImageField(
        max_length=None, use_url=True, required=False)

    class Meta:
        model = Doctor
        fields = ('complete_name', 'especialization', 'photo')


class Doctor_id_serializer(serializers.ModelSerializer):
    photo = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Doctor
        fields = ('id', 'complete_name', 'especialization', 'photo')


class Patient_serializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = ('id', 'complete_name', 'rg', 'birth_date',
                  'number_for_contact1', 'number_for_contact2', 'email')


class Medical_appointment_serializer(serializers.ModelSerializer):
    file_related = serializers.FileField(
        max_length=None, use_url=True, required=False)

    class Meta:
        model = Medical_appointment
        fields = ('patient', 'doctor', 'state', 'date', 'file_related')


class Medical_appointment_id_serializer(serializers.ModelSerializer):
    file_related = serializers.FileField(
        max_length=None, use_url=True, required=False)
    patient = serializers.StringRelatedField()
    doctor = serializers.StringRelatedField()

    class Meta:
        model = Medical_appointment
        fields = ('id', 'patient', 'doctor', 'state', 'date', 'file_related')
