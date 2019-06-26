<template>
  <div id="upload">
    <div class="row">
      <div class="col-sm-12">
        <div class="col-sm-12">
          <h2 class="h2 py-3 border-bottom">Uploading a CSV File</h2>
          <h5 class="h5 py-5">To upload a CSV file, please make sure to follow these simple rules:</h5>
          <ul class="list-group ml-5">
            <li class="list-group-item">Header Row Is Present</li>
            <li
              class="list-group-item"
            >Column Order Is: First Name (String), Last Name (String), Group ID (int), Role ID (int)</li>
            <li class="list-group-item">More here</li>
          </ul>
        </div>
        <div class="col-sm-12 text-center mt-5">
          <button type="button" class="btn btn-primary">Select CSV File</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "uploads",
  data() {
    return {};
    /*
    show loading svg until promise returns either success or failure and show error message if it fails...general error message
    */
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
