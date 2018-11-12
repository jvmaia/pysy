# Pysy API Documentation
  >Pysy is composed by an api made with Django Rest Framework and a client made using Vuejs2 and bootstrap.
  
  >You can see a demo video of this project working on https://goo.gl/HVjkM5

### Running
    - docker-compose up --build
    - docker-compose exec web python3 manage.py createsuperuser
    - docker-compose exec web python3 manage.py makemigrations pysy_api
    - docker-compose exec web python3 manage.py migrate
    - docker-compose exec web npm run dev

### /api/api-token-auth
    - POST - Return a token for account posted

### /api/doctors 
    - GET -  Return a list of doctors
    - POST -  Create a new doctor

### /api/doctors/changes/[0-9]
    - DELETE - Delete a doctor identified by a id passed in url
    - PUT - Modify a doctor identified by a id passed in url

### /api/patients
    - GET - Return a list of patients
    - POST - Create a new patient

### /api/patients/changes/[0-9]
    - DELETE - Delete a patient identified by a id passed in url
    - PUT - Modify a patient identified by a id passed in url

### /api/medicalapps
    - GET - Return a list of medical appointments
    - POST - Create a new medical appointment
    
### /api/[0-9]/medicalapp
    - GET - Return a list of specifical medical appointments based on doctor id in url
    - PUT - Modify a medical appointment identified by a id passed in url
    - DELETE - Delete a medical appointment identified by a id passed in url
