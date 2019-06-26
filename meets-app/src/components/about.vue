<template>
  <div id="about">
    <div class="row">
      <div class="col-sm-12">
        <h2>JC Meets</h2>
        <p>JC meets is sample SPA that uses a Python Flask API backend with a Vue.JS Front end. Its only requirements are CRUD actions on groups.</p>
      </div>
      <div v-if="loading" class="col-sm-12 text-center mt-5">
        <img src="../../static/images/svg_loader.svg" height="150">
      </div>
      <div v-else v-for="(x, index) in groups" :key="index" class="col-lg-4">
        <div class="card text-center mt-3">
          <div class="card-body">
            <h5 class="card-title">{{x.Group_Name}}</h5>
            <p class="card-text">Group Description would go here normally..</p>
            <a href="#" class="btn btn-primary">Join Group</a>
          </div>
        </div>
        <!-- end card -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "about",
  data() {
    return {
      loading: true,
      groups: [],
      users: []
    };
  },
  mounted() {
    axios.get("http://localhost:5000/group").then(response => {
      this.groups = response.data;
      this.loading = false;
    });
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
