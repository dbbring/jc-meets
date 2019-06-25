<template>
  <div id="main-app">
    <div class="container-fluid">
      <div class="row bg-dark py-5">
        <div class="col-sm-12 text-white text-right">
          <h1>{{sections[activeSection]}}</h1>
        </div>
      </div>
      <div class="row">
        <div class="col-md-3 bg-danger" style="height: 75vH;">
          <ul>
            <li v-for="x in sections" :key="x">{{x}}</li>
          </ul>
          <div style="position:absolute;bottom:15px;">
            <button type="button" class="btn btn-primary text-warning">Upload CSV</button>
          </div>
        </div>
        <div class="col-md-9">
          <groups></groups>
          <!-- groups, users, etc components here-->
        </div>
      </div>
    </div>
    <!--End container fluid-->
  </div>
</template>

<script>
import groups from "./components/Groups";

export default {
  name: "meetsApp",
  data() {
    return {
      sections: ["About JC Meets", "Groups", "Users", "Roles"],
      activeSection: 0
    };
  },
  components: {
    groups
  },
  methods: {
     toggleSection (newSection) {
      
    }
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
