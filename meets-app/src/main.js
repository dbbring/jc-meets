import Vue from "vue";
import meetsApp from "./meetsApp.vue";
import store from "./store";

Vue.config.productionTip = false;

new Vue({
  store,
  render: h => h(meetsApp)
}).$mount("#meetsApp");
