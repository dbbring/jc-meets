<template>
  <div id="users">
    <div class="row">
      <div v-if="loading" class="col-sm-12 text-center mt-5">
        <img src="../../static/images/svg_loader.svg" height="150">
      </div>
      <div v-else v-for="(x,index) in users" :key="index" class="col-lg-3 mt-3">
        <div class="card" style="max-width: 18rem;">
          <div class="card-body">
            <h5 class="card-title">{{x.User_First_Name}}</h5>
            <h6 class="card-subtitle mb-2 text-muted">{{x.User_Last_Name}}</h6>
            <p class="card-text">User Description would go here....</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "users",
  data() {
    return {
      loading: false,
      users: []
    };
  },
  mounted() {
    axios.get("http://localhost:5000/user").then(response => {
      this.users = response.data;
      this.loading = false;
    });
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
