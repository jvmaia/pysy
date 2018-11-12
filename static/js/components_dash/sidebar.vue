<template>
  <div id="sidebar">
    <div class="col-sm-3 col-md-2 sidebar">
      <ul class="nav nav-sidebar">
          <li class="active"><a href="#">Overview <span class="sr-only">(current)</span></a></li>
          <li><a href="#">Reports</a></li>
          <li><a href="#">Analytics</a></li>
          <li><a href="#">Export</a></li>
        </ul>
      <ul class="nav nav-sidebar">
        <li><a href="#" v-on:click="view_s('view_appointments')">View Medicalapps</a></li>
        <li><a href="#" v-on:click="view_s('view_patients')">View Patients</a></li>
        <li><a href="#" v-on:click="view_s('create_appointment')">Create Medicalapp</a></li>
        <li><a href="#" v-on:click="view_s('create_patient')">Create Patient</a></li>
        <li><a href="#" v-on:click="view_s('create_doctor')">Create Doctor</a></li>
      </ul>
      <ul class="nav nav-sidebar">
        <li><a href="#">Nav item again</a></li>
        <li><a href="#">One more nav</a></li>
        <li><a href="#">Another nav item</a></li>
      </ul>
    </div>
  </div>
</template>

<script>

export default{
  data(){
    return{
      // something
    }
  },
  mounted(){
    // something
  },
  methods: {
    view_s: function(option){
      Event.$emit('view_something', [option])
    },
  }
}

</script>
