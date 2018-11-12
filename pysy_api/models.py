from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Patient(models.Model):
    complete_name = models.CharField(max_length=60)
    rg = models.CharField(max_length=12)
    birth_date = models.DateField()
    number_for_contact1 = models.CharField(max_length=12)
    number_for_contact2 = models.CharField(max_length=12)
    email = models.EmailField(max_length=30, blank=True)

    def __str__(self):
        return self.complete_name


class Doctor(models.Model):
    complete_name = models.CharField(max_length=60)
    especialization = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='photos/', default='photos/teste.jpg')

    def __str__(self):
        return self.complete_name


class State(models.Model):
    name = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return self.name


class Medical_appointment(models.Model):
    file_related = models.FileField(upload_to='exams/', default='null.pdf')
    patient = models.ForeignKey(Patient)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    state = models.ForeignKey(State)
    date = models.DateTimeField()

    def __str__(self):
        return self.patient.complete_name + "/" + self.doctor.complete_name

    def next_appointments(self):
        now = timezone.now()
        return now <= self.date
    next_appointments.admin_order_field = 'next_appointments'
    next_appointments.boolean = True
    next_appointments.short_description = 'Next appointments'
