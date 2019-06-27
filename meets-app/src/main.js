import Vue from "vue";
import meetsApp from "./meetsApp";
import store from "./store";

Vue.config.productionTip = false;

new Vue({
  el: "#jc-meets",
  store,
  components: { meetsApp },
  template: "<meetsApp/>"
});
