<template>
  <div id="doc_placeholders" v-if="this.type === 'on'">
    <div v-for="doctor in doctors">
      <div class="col-xs-6 col-sm-3 placeholder">
        <img :src="doctor.photo" v-on:click="choose_doctor(doctor.id)"  id="clickable" width="200" height="200" class="img-responsive" alt="Generic placeholder thumbnail">
        <h4> {{ doctor.complete_name }}</h4>
        <span class="text-muted">{{ doctor.especialization }}</span>
      </div>
    </div>
  </div>
</template>

<script>

export default{
  data(){
    return{
      type: "on",
      doctors: [],
      config: {
        headers:{}
      },
    }
  },
  mounted(){
    this.config.headers.responseType = "json"
    this.config.headers.Authorization = "Token " + this.$cookie.get('token')
    this.axios.get("/api/doctors/", this.config).then( (res) => this.doctors = res.data)
  },
  methods: {
    choose_doctor: function(doctor_id){
      Event.$emit('choose_doctor', [doctor_id])
    },
    reload_doctors: function(){
      this.axios.get("/api/doctors/", this.config).then( (res) => this.doctors = res.data)
    },
    change_type: function(option){
      if (option[0] != "view_appointments"){
        this.type = "off"
      }
      else{
        this.type = "on"
      }
    },
  },
  created() {
    Event.$on('change_doctors', (doctor_id) => this.reload_doctors());
    Event.$on('view_something', (option) => this.change_type(option));
  }
}
</script>
