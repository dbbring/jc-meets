<template>
  <div id="upload">
    <div class="row">
      <div class="col-sm-12">
        <div v-if="loading" class="col-sm-12 text-center mt-5">
          <img src="../../static/images/svg_loader.svg" height="150">
        </div>
        <div v-else class="col-sm-12">
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
        <div v-if="!loading" class="col-sm-12 text-center mt-5">
          <input type="file" id="file" @change="checkFile($event)" title="Upload CSV File">
          <label for="file" class="btn-2">Upload</label>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import papa from "papaparse";

export default {
  name: "uploads",
  data() {
    return {
      loading: false
    };
  },
  methods: {
    checkFile(event) {
      this.loading = true;
      // Get file from input
      const file = event.target.files[0];
      papa.parse(file, {
        delimiter: ",",
        header: true,
        // Will convert strings to dates and numbers
        dynamicTyping: true,
        complete: results => {
          if (results.errors.length > 0) {
            console.log(results);
            return;
          }
          console.log(results.data);
          this.loading = false;
        }
      });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
[type="file"] {
  height: 0;
  overflow: hidden;
  width: 0;
}

[type="file"] + label {
  background: #f15d22;
  border: none;
  border-radius: 5px;
  color: #fff;
  cursor: pointer;
  display: inline-block;
  font-size: inherit;
  font-weight: 600;
  margin-bottom: 1rem;
  outline: none;
  padding: 1rem 50px;
  position: relative;
  transition: all 0.3s;
  vertical-align: middle;

  &.btn-2 {
    background-color: #99c793;
    border-radius: 50px;
    overflow: hidden;

    &::before {
      color: #fff;
      content: "\f382";
      font-family: "Font Awesome 5 Free";
      font-size: 100%;
      height: 100%;
      right: 130%;
      line-height: 3.3;
      position: absolute;
      top: 0px;
      transition: all 0.3s;
    }

    &:hover {
      background-color: darken(#99c793, 30%);

      &::before {
        right: 75%;
      }
    }
  }
}
</style>
