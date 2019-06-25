<template>
  <div id="about">
    <h2>JC Meets</h2>
    <p>JC meets is sample SPA that uses a Python Flask API backend with a Vue.JS Front end. Its only requirements are CRUD actions on groups.</p>
  </div>
</template>

<script>
export default {
  name: "about",
  data() {
    return {
      msg: "Welcome to Your Vue.js App"
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
