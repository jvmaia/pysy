"""pysy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from rest_framework.authtoken import views as rest_views
from . import views

urlpatterns = [
    url(r'^api-token-auth/$', rest_views.obtain_auth_token),
    url(r'^states/$', views.StateList.as_view(), name='states'),
    url(r'^doctors/$', views.DoctorList.as_view(), name='doctors'),
    url(r'^doctors/changes/(?P<pk>[0-9]+)/$',
        views.DoctorChanges.as_view(), name='doctors changes'),
    url(r'^patients/$', views.PatientList.as_view(), name='patients'),
    url(r'^patients/changes/(?P<pk>[-\w]+)/$',
        views.PatientChanges.as_view(), name='patients changes'),
    url(r'^medicalapps/$', views.MedicalappsList.as_view(), name='medicalapps'),
    url(r'^(?P<pk>[0-9]+)/medicalapp/$',
        views.MedicalApp.as_view(), name='medicalapp')
]
