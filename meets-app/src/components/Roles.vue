<template>
  <div id="roles">
    <div class="row">
      <div v-if="loading" class="col-sm-12 text-center mt-5">
        <img src="../../static/images/svg_loader.svg" height="150">
      </div>
      <div v-else-if="isError" class="col-sm-12 text-center mt-5">
        <h5 class="h5 text-danger">There was a Error Submitting Your Request.</h5>
      </div>
      <div v-else v-for="(x,index) in roles" :key="index" class="col-lg-12 mt-3">
        <div class="card">
          <div class="card-header">Required Role</div>
          <div class="card-body">
            <h5 class="card-title">{{x.Role_Name}}</h5>
            <p class="card-text">{{x.Role_Descrip}}</p>
            <a href="#" class="btn btn-primary">View Members</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "roles",
  data() {
    return {
      loading: true,
      isError: false,
      roles: []
    };
  },
  mounted() {
    axios
      .get("http://localhost:5000/role")
      .then(response => {
        this.roles = response.data;
        this.loading = false;
      })
      .catch(() => {
        this.loading = false;
        this.isError = true;
      });
  }
};
</script>

<style scoped>
</style>
