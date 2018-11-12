from django.contrib import admin
from .models import Patient, Medical_appointment, Doctor, State

class PatientAdmin(admin.ModelAdmin):
    list_display = ('complete_name', 'birth_date')

class Medical_appointmentAdmin(admin.ModelAdmin):
    fieldsets = [
            ('Patient', {
                'fields': ['patient']
                }),
            ('Doctor', {
                'fields': ['doctor']
                }),
            ('Medical Appointment', {
                'fields': ['state', 'date', 'file_related']
                })
    ]
    list_display = ('patient', 'date', 'doctor')
    list_filter = ['date']
    search_fields = ['patient']

admin.site.register(Patient, PatientAdmin)
admin.site.register(Medical_appointment, Medical_appointmentAdmin)
admin.site.register(Doctor)
admin.site.register(State)
