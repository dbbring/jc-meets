<template>
  <div id="main-app">
    <div class="container-fluid">
      <div
        class="row py-5"
        style="background:url(../static/images/jc-meets-header.jpg) center center no-repeat; background-size: cover;"
      >
        <!-- set title based on fragement displayed -->
        <div class="col-sm-12 text-white text-right">
          <h1>{{sections[activeSection].title}}</h1>
        </div>
      </div>
      <div class="row">
        <nav class="navbar navbar-light bg-warning w-100" id="hamMenu" @click="showMenu()">
          <button class="navbar-toggler" type="button">
            <span class="navbar-toggler-icon"></span>
          </button>
        </nav>
        <div
          :class="{showHiddenMenu : showMenuDiv}"
          class="col-md-3 bg-danger"
          style="height: 75vH;"
          id="menu"
        >
          <div class="list-group mt-4">
            <!-- populate sidebar menu -->
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
        </div>
      </div>
    </div>
    <!--End container fluid-->
  </div>
</template>

<script>
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
      showMenuDiv: false,
      showMobileToggle: true,
      sections: [
        { title: "About JC Meets", show: true },
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
    @params -> int, index number of section to be displayed. 0 is about, 1 is upload, 2 is groups, 3 is users, 4 is roles
    @return -> none
    */
    toggleSection(newSection) {
      this.sections[this.activeSection].show = false;
      this.sections[newSection].show = true;
      this.activeSection = newSection;
      if (window.innerWidth < 767) {
        this.showMenuDiv = false;
      }
      return;
    },
    showMenu() {
      this.showMenuDiv = !this.showMenuDiv;
    }
  },
  mounted() {
    if (window.innerWidth > 767) {
      this.showMenuDiv = true;
      this.showMobileToggle = false;
    }
  }
};
</script>

<style>
@media screen and (max-width: 767px) {
  #menu {
    display: none;
  }

  #hamMenu {
    display: block !important;
  }

  .showHiddenMenu {
    display: block !important;
  }
}

#hamMenu {
  display: none;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>
