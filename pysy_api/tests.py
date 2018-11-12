from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.utils import timezone
from .models import Doctor, Medical_appointment, Patient, State


password = 'testeitei'
my_admin = User.objects.create_superuser('myttest', 'teste@teste.tes', password)

class PatientTests(APITestCase):
    def test_get_patients(self):
        self.client.force_authenticate(user=my_admin)
        url = '/api/patients/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_patient(self):
        """
        ensure we can create a new patient object
        """
        self.client.force_authenticate(user=my_admin)
        data =  {'complete_name': 'por favor funciona', 'rg':'13245678',
                'birth_date': '3001-01-01', 'number_for_contact1':'12123456789',
                'number_for_contact2':'12132465788', 'email':'test@tst.tst'}
        url = '/api/patients/'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class DoctorTests(APITestCase):
    def test_create_doctor(self):
        """
        ensure we can create a new doctor object
        """
        self.client.force_authenticate(user=my_admin)
        url ='/api/doctors/'
        filename = './teste_py.png'
        with open(filename, 'rb') as f_post:
            response = self.client.post(url, {'complete_name':'por favor funciona', 'especialization':'working', 'photo': f_post})
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class Medical_appTests(APITestCase):
    def test_create_medicalapp(self):
        """
        ensure we can create a medical appointment object
        """
        state = State('Encaixe')
        state.save()
        doctor = Doctor(complete_name='teste vuejs7', especialization='vuejs7')
        doctor.save()
        patient = Patient(complete_name='por favor funciona', rg='1234567', birth_date='2000-05-09',
         number_for_contact1='12132456789', number_for_contact2='12132456788', email='teste@teste.tstt')
        patient.save()
        self.client.force_authenticate(user=my_admin)
        filename = './teste.txt'
        url = '/api/medicalapps/'
        with open(filename, 'rb') as fl:
            response = self.client.post(url, {'patient':patient.complete_name,
            'doctor':doctor.id, 'state':'Encaixe', 'date':'2018-01-01 06:00:00', 'file_related':fl})
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_medicalapp(self):
        """
        ensure we can delete a medical appointment object
        """
        state = State('Encaixe')
        state.save()
        doctor = Doctor(complete_name='teste vuejs7', especialization='vuejs7')
        doctor.save()
        patient = Patient(complete_name='por favor funciona', rg='1234567', birth_date='2000-05-09',
         number_for_contact1='12132456789', number_for_contact2='12132456788', email='teste@teste.tstt')
        patient.save()
        medicalapp = Medical_appointment(patient=patient, doctor=doctor, state=state, date='2020-01-01 06:00:00')
        medicalapp.save()
        self.client.force_authenticate(user=my_admin)
        response = self.client.delete('/api/{}/medicalapp/'.format(medicalapp.id))
        self.assertEqual(response.status_code, 200)
