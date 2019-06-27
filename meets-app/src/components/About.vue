<template>
    <div id="about">
      <div class="row">
        <div v-if="isError" class="col-sm-12 text-center mt-5">
          <h5 class="h5 text-danger">There was a Error Submitting Your Request.</h5>
        </div>
        <div v-else class="col-sm-12">
          <h2>JC Meets</h2>
          <p>
            JC meets is sample single page application that uses a API interface to interact with a SQLite backend. I have tried to make a clear seperation of duties here
            in regards to back-end and front-end. You can simply rewrite the front-end in your langauge of choice and make the required API calls, or rewrite the RESTful API
            on the back-end and keep the front-end the same. Either way, this is a sample application running a Vue.JS Front-end, Python Flask RESTful API, and SQLite Back-end.
          </p>
          <br>Although I have roughly 15 hours into this project, I feel that if I had more time I would implement these changes:
          <ul class="list-group mx-auto my-4" style="max-width: 500px;">
            <li class="list-group-item list-group-item-info">Better Error Coverage</li>
            <li
              class="list-group-item list-group-item-info"
            >Break Down Front-End, Kind of Messy Currently</li>
            <li class="list-group-item list-group-item-info">Handle User Role Insertion from CSV</li>
            <li
              class="list-group-item list-group-item-info"
            >Handle Responses From Server to Keep User Informed</li>
            <li class="list-group-item list-group-item-info">Account For More Edge Cases</li>
          </ul>
        </div>
      </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
  name: "about",
  data() {
    return {};
  }
};
</script>

<style scoped>
</style>
