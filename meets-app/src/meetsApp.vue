<template>
  <div id="main-app">
    <div class="container-fluid">
      <div
        class="row py-5"
        style="background:url(../static/images/jc-meets-header.jpg) center center no-repeat; background-size: cover;"
      >
        <div class="col-sm-12 text-white text-right">
          <h1>{{sections[activeSection].title}}</h1>
        </div>
      </div>
      <div class="row">
        <div class="col-md-3 bg-danger" style="height: 75vH;">
          <div class="list-group mt-4">
            <a
              href="#"
              class="list-group-item list-group-item-action bg-danger text-white"
              v-for="(x, index) in sections"
              :key="index"
              @click="toggleSection(index)"
            >{{x.title}}</a>
          </div>
        </div>
        <div class="col-md-9">
          <about v-if="sections[0].show"></about>
          <uploads v-if="sections[1].show"></uploads>
          <groups v-if="sections[2].show"></groups>
          <users v-if="sections[3].show"></users>
          <roles v-if="sections[4].show"></roles>
          <!-- groups, users, etc components here-->
        </div>
      </div>
    </div>
    <!--End container fluid-->
  </div>
</template>

<script>
/*
Fire up dev server... navigate to jc-meets/api/api and run  python -m pip install -r requirements.txt ... then run python routes.py
*/
import groups from "./components/Groups";
import users from "./components/Users";
import roles from "./components/Roles";
import uploads from "./components/Uploads";
import about from "./components/About";
import axios from "axios";

export default {
  name: "meetsApp",
  data() {
    return {
      sections: [
        { title: "About JC Meets", show: false },
        { title: "Upload Data", show: false },
        { title: "Groups", show: false },
        { title: "Users", show: false },
        { title: "Roles", show: false }
      ],
      activeSection: 0
    };
  },
  components: {
    groups,
    users,
    roles,
    uploads,
    about
  },
  methods: {
    /*
    Use vuex store to manage state of data like populate store with api calls and modifiy state which then commits a api call. 
     */
    toggleSection(newSection) {
      this.sections[this.activeSection].show = false;
      this.sections[newSection].show = true;
      this.activeSection = newSection;
    }
  },
  mounted() {
    let self = this;
    axios.get("http://localhost:5000/group").then(response => {
      self.$store.commit("setData", response.data);
    });
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
