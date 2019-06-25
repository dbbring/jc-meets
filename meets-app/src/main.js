// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue";
import meetsApp from "./meetsApp";
import store from "./store";

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: "#jc-meets",
  store,
  components: { meetsApp },
  template: "<meetsApp/>"
});
