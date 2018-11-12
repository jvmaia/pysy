from django.shortcuts import render
from rest_framework.authtoken.models import Token


def dashboard(request):
	try:
		token = Token.objects.get(key=request.COOKIES['token'])
		return render(request, "pysy_client/dashboard.html")
	except (Token.DoesNotExist, KeyError):
		return render(request, "pysy_client/login.html")
