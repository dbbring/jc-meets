<template>
  <div id="users">
    <div class="row">
      <div v-if="loading" class="col-sm-12 text-center mt-5">
        <img src="svg_loader.svg" height="150" />
      </div>
      <div v-else-if="isError" class="col-sm-12 text-center mt-5">
        <h5 class="h5 text-danger">
          There was a Error Submitting Your Request.
        </h5>
      </div>
      <div
        v-else
        v-for="(x, index) in users"
        :key="index"
        class="col-lg-3 mt-3"
      >
        <div class="card" style="max-width: 18rem;">
          <div class="card-body">
            <h5 class="card-title">{{ x.User_First_Name }}</h5>
            <h6 class="card-subtitle mb-2 text-muted">
              {{ x.User_Last_Name }}
            </h6>
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
      isError: false,
      users: []
    };
  },
  mounted() {
    axios
      .get("http://localhost:5000/user")
      .then(response => {
        this.users = response.data;
        this.loading = false;
      })
      .catch(() => {
        this.loading = false;
        this.isError = true;
      });
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
