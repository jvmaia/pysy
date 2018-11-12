<template>
  <div id="dash" v-if="this.type === 'view_appointments'">
    <h2 class="sub-header" v-on:click="reload()" id="clickable">Medical Appointments</h2>
    <table class="table table-striped">
      <thead>
        <tr>
          <th>Patient</th>
          <th>Doctor</th>
          <th>State</th>
          <th>Date</th>
          <th>Modify</th>
          <th>Delete</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="medicalapp in medicalapps" v-bind:id="'medicalapp'+medicalapp.id">
          <td>{{ medicalapp.patient }}</td>
          <td>{{ medicalapp.doctor }}</td>
          <td>{{ medicalapp.state }}</td>
          <td>{{ medicalapp.date.split("T").join(" ") + ":00" }}</td>
          <td v-on:click="modify_medicalapp_View(medicalapp)" class="text-warning warning"> Modify </td>
          <td v-on:click="delet(medicalapp.id)" class="text-danger warning"> Del </td>
        </tr>
      </tbody>
    </table>
  </div>

  <div id="dash" v-else-if="this.type === 'view_patients'">
    <h2 class="sub-header">View Patients</h2>
    <table class="table table-striped">
      <thead>
        <th>Complete name</th>
        <th>Rg</th>
        <th>Birth date</th>
        <th>Number for contact 1</th>
        <th>Number for contact 2</th>
        <th>Email</th>
        <th>Modify</th>
      </thead>
      <tbody>
        <tr v-for="patient in patients">
          <td>{{ patient.complete_name }}</td>
          <td>{{ patient.rg }}</td>
          <td>{{ patient.birth_date }}</td>
          <td>{{ patient.number_for_contact1 }}</td>
          <td>{{ patient.number_for_contact2 }}</td>
          <td>{{ patient.email }}</td>
          <td v-on:click="modify_patient_View(patient)" class="text-warning"> Modify </td>
        </tr>
      </tbody>
    </table>
  </div>

  <div id="dash" v-else-if="this.type === 'create_appointment'">
      <h2 class="sub-header">Create Medical appointment</h2>
      <br>
      <form name="medicalappointment" onsubmit="return false">
        <p>Patient:
          <select v-model="selected.medical_appointment.patient">
            <option v-for="patient in patients" v-bind:value="patient.id">
              {{ patient.complete_name }}
            </option>
          </select>
        </p>
        <p>Doctor:
          <select v-model="selected.medical_appointment.doctor">
            <option v-for="doctor in doctors" v-bind:value="doctor.id">
              {{ doctor.complete_name }}
            </option>
          </select>
        </p>
        <p>State:
          <select v-model="selected.medical_appointment.state">
            <option v-for="state in states" v-bind:value="state.name">
              {{ state.name }}
            </option>
          </select>
        </p>
        <p>Date:
          <input v-model="selected.medical_appointment.date" type="datetime-local">
        </p>
        <p>Exam file:
          <input v-on:change="exam_change($event)" type="file" id="exam">
        </p>
        <button v-on:click="create_medicalappointment()" type="button" class="btn btn-primary">Create</button>
      </form>
      <p>{{ status_message }}</p>
  </div>

  <div id="dash" v-else-if="this.type === 'create_doctor'">
    <h2 class="sub-header">Create Doctor</h2>
    <form name="doctor" onsubmit="return false">
      <p>Complete name:
        <input v-model="selected.doctor.complete_name" type="text">
      </p>
      <p>Especialization
        <input v-model="selected.doctor.especialization" type="text">
      </p>
      <p>Photo:
        <input v-on:change="photo_change($event)" type="file" id="photo">
      </p>

      <button v-on:click="create_doctor()" type="button" class="btn btn-primary">Create</button>
    </form>
    <p>{{ status_message }}</p>
  </div>

  <div id="dash" v-else-if="this.type === 'create_patient'">
      <h2 class="sub-header">Create Patient</h2>
      <br>
      <form name="patient" onsubmit="return false">
        <p>Complete name:
          <input v-model="selected.patient.complete_name" type="text">
        </p>
        <p>Rg:
          <input v-model="selected.patient.rg" type="number">
        </p>
        <p>Birth date:
          <input v-model="selected.patient.birth_date" type="date">
        </p>
        <p>Number for contact 1:
          <input v-model="selected.patient.number_for_contact1" type="number">
        </p>
        <p>Number for contact 2:
          <input v-model="selected.patient.number_for_contact2" type="number">
        </p>
        <p>Email:
          <input v-model="selected.patient.email" type="email">
        </p>

        <button v-on:click="create_patient()" type="button" class="btn btn-primary">Create</button>
      </form>
      <p>{{ status_message }}</p>
  </div>

  <div id="dash" v-else-if="this.type === 'modify_medicalapp'">
    <h2 class="sub-header">Modify Medical appointment</h2>
    <br>
    <form name="medicalappointment" onsubmit="return false">
      <p>Patient:
        <select v-model="medicalapp.patient.complete_name">
          <option v-for="patient in patients" v-bind:value="patient.id">
            {{ patient.complete_name }}
          </option>
        </select>
      </p>
      <p>Doctor:
        <select v-model="medicalapp.doctor.complete_name">
          <option v-for="doctor in doctors" v-bind:value="doctor.id">
            {{ doctor.complete_name }}
          </option>
        </select>
      </p>
      <p>State:
        <select v-model="medicalapp.state">
          <option v-for="state in states" v-bind:value="state.name">
            {{ state.name }}
          </option>
        </select>
      </p>
      <p>Date:
        <input v-model="medicalapp.date" type="datetime-local">
      </p>
      <p>Exam file:
        <input v-on:change="exam_change($event)" type="file" id="exam">
      </p>
      <button v-on:click="modify_medicalapp()" type="button" class="btn btn-primary">Modify</button>
    </form>
    <p>{{ status_message }}</p>
  </div>

  <div id="dash" v-else-if="this.type === 'modify_patient'">
    <h2 class="sub-header">Modify Patient</h2>
    <br>
    <form name="patient" onsubmit="return false">
      <p>Complete name:
        <input v-model="patient.complete_name" type="text">
      </p>
      <p>Rg:
        <input v-model="patient.rg" type="number">
      </p>
      <p>Birth date:
        <input v-model="patient.birth_date" type="date">
      </p>
      <p>Number for contact 1:
        <input v-model="patient.number_for_contact1" type="number">
      </p>
      <p>Number for contact 2:
        <input v-model="patient.number_for_contact2" type="number">
      </p>
      <p>Email:
        <input v-model="patient.email" type="email">
      </p>

      <button v-on:click="modify_patient()" type="button" class="btn btn-primary">Modify</button>
    </form>
    <p>{{ status_message }}</p>
  </div>

</template>

<script>

export default{
  data(){
    return{
      type: "view_appointments",
      status_message: undefined,
      selected: {
        medical_appointment: {
          patient: undefined,
          doctor: undefined,
          state: undefined,
          date: undefined,
          file_related: undefined,
        },
        patient: {
          complete_name: undefined,
          rg: undefined,
          birth_date: undefined,
          number_for_contact1: undefined,
          number_for_contact2: undefined,
          email: undefined
        },
        doctor: {
          complete_name: undefined,
          especialization: undefined,
          photo: undefined,
        }
      },
      medicalapps: [],
      doctors: [],
      patients: [],
      states: [],
      config: {
        headers:{}
      },
      patient: {},
      medicalapp: {}
    }
  },
  mounted(){
    this.config.headers.Authorization = "Token " + this.$cookie.get('token');
    this.axios.get("/api/medicalapps/", this.config).then( (res) => this.medicalapps = res.data)
    .catch(e =>{
      console.log(e);
    });

    this.axios.get("/api/doctors/", this.config).then( (res) => this.doctors = res.data)
    .catch(e =>{
      console.log(e);
    });

    this.axios.get("/api/patients/", this.config).then( (res) => this.patients = res.data)
    .catch(e =>{
      console.log(e);
    });

    this.axios.get("/api/states/", this.config).then( (res) => this.states = res.data)
    .catch(e =>{
      console.log(e);
    });
  },
  methods: {
    change_type: function(option){
      if (option[0] === "view_appointments"){
        this.type = "view_appointments"
        this.reload()
      }
      else if (option[0] === "view_patients") {
        this.type = "view_patients"
        this.axios.get("/api/patients/", this.config).then( (res) => this.patients = res.data)
      }
      else if (option[0] === "create_patient"){
        this.type = "create_patient"
      }
      else if (option[0] === "create_appointment"){
        this.type = "create_appointment"
      }
      else if (option[0] === "create_doctor") {
        this.type = "create_doctor"
      }
    },
    exam_change: function(event){
      this.selected.medical_appointment.file_related = event.target.files[0]
    },
    photo_change: function(event){
      this.selected.doctor.photo = event.target.files[0]
    },
    delet: function(id_medicalapp){
      this.config.headers.responseType = "json";
      this.axios.delete("/api/" + id_medicalapp + "/medicalapp/", this.config).then( (res) => this.reload());
    },
    reload: function(id_doctor = undefined){
      this.config.headers.responseType = "json";
      if (id_doctor){
        this.axios.get("/api/" + id_doctor + "/medicalapp/", this.config).then( (res) => this.medicalapps = res.data)
        .catch( (e) => console.log(e) );
      }
      else{
        this.axios.get("/api/medicalapps/", this.config).then( (res) => this.medicalapps = res.data)
        .catch( (e) => console.log(e) );
      }
      this.type = "view_appointments"
    },
    create_medicalappointment: function(){
      this.status_message = "Creating medical appointment...";
      var formData = new FormData()
      var exam = document.querySelector("#exam")
      if (exam.files[0] != undefined){
        formData.append("file_related", exam.files[0])
      }
      formData.append("patient", this.selected.medical_appointment.patient)
      formData.append("doctor", this.selected.medical_appointment.doctor)
      formData.append("state", this.selected.medical_appointment.state)
      formData.append("date", this.selected.medical_appointment.date.split("T").join(" ") + ":00")
      this.selected.medical_appointment.patient = undefined;
      this.selected.medical_appointment.doctor = undefined;
      this.selected.medical_appointment.state = undefined;
      this.selected.medical_appointment.date = undefined;
      this.axios.post('/api/medicalapps/', formData, this.config)
      .then(function (response){
        confirm("Medical Appointment created with success");
        Event.$emit('view_something', ['view_appointments']);
      })
    },
    create_doctor: function(){
      this.status_message = "Creating doctor...";
      var formData = new FormData()
      var photo = document.querySelector("#photo")
      formData.append("photo", photo.files[0])
      formData.append("complete_name", this.selected.doctor.complete_name)
      formData.append("especialization", this.selected.doctor.especialization)
      this.selected.doctor.complete_name = undefined;
      this.selected.doctor.especialization = undefined;
      this.axios.post('/api/doctors/', formData, this.config)
      .then(function (response){
        confirm("Doctor created with success")
        Event.$emit('view_something', ['view_appointments']);
        Event.$emit('change_doctors');
      })
    },
    create_patient: function(){
      this.status_message = "Creating patient...";
      var formData = new FormData();
      formData.append("complete_name", this.selected.patient.complete_name)
      formData.append("rg", this.selected.patient.rg)
      formData.append("birth_date", this.selected.patient.birth_date)
      formData.append("number_for_contact1", this.selected.patient.number_for_contact1)
      formData.append("number_for_contact2", this.selected.patient.number_for_contact2)
      formData.append("email", this.selected.patient.email)
      this.selected.patient.complete_name = undefined;
      this.selected.patient.rg = undefined;
      this.selected.patient.birth_date = undefined;
      this.selected.patient.number_for_contact1 = undefined;
      this.selected.patient.number_for_contact2 = undefined;
      this.selected.patient.email = undefined;
      this.axios.post('/api/patients/', formData, this.config)
      .then(function (response){
        confirm("Patient created with success");
        Event.$emit('view_something', ['view_patients']);
      })
    },
    modify_medicalapp_View: function(medicalapp){
      this.type = "modify_medicalapp";
      this.medicalapp = medicalapp;
    },
    modify_patient_View: function(patient){
      this.type = "modify_patient";
      this.patient = patient;
    },
    modify_patient: function(){
      this.axios.put("/api/patients/changes/"+this.patient.id+"/", this.patient, this.config)
        .then(function(response){
          confirm('Patient changed with success');
          Event.$emit('view_something', ['view_patients']);
        })
        .catch(function(error){
          confirm('Something very very bad occurred please run to the mountains');
          console.log(error);
        })
    },
    modify_medicalapp: function(){
      var medicalapp = this.medicalapp;
      medicalapp.date = this.medicalapp.date.split("T").join(" ") + ":00";
      delete medicalapp.file_related;
      this.axios.put("/api/"+this.medicalapp.id+"/medicalapp/", medicalapp, this.config)
        .then(function(response){
          confirm('Medical appointment changed with success');
          Event.$emit('view_something', ['view_appointments']);
        })
        .catch(function(error){
          confirm('Something very very bad occurred please run to the mountains');
          console.log(error);
        })
    }
  },
  created() {
    Event.$on('choose_doctor', (doctor_id) => this.reload(doctor_id));
    Event.$on('view_something', (option) => {
      this.status_message = "";
      this.change_type(option);
    });
  }
}
</script>
