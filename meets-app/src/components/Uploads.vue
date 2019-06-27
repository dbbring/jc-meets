<template>
  <div id="upload">
    <div class="row">
      <!-- Error block for exceptions -->
      <div v-if="isError" class="col-sm-12 text-center mt-5">
        <h5 class="h5 text-danger">{{errorMsg}}</h5>
        <button type="button" class="btn btn-danger" @click="isError = false">Ok</button>
      </div>
      <div v-else class="col-sm-12">
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
            >Column Order Is: First_Name (String) ,Last_Name (String), Group_Name(String), Role_ID(int)</li>
            <li class="list-group-item">More here</li>
          </ul>
        </div>
        <div v-if="!loading" class="col-sm-12 text-center mt-5">
          <input
            type="file"
            id="file"
            @change="checkFile($event)"
            title="Upload CSV File"
            accept=".csv"
          >
          <label for="file" class="btn-2">Upload</label>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import papa from "papaparse";
import axios from "axios";

export default {
  name: "uploads",
  data() {
    return {
      isError: false,
      errorMsg: "There was a Error Submitting Your Request.",
      loading: false,
      exportJSON: {
        Upload_Array: []
      }
    };
  },
  methods: {
    checkFile(event) {
      this.loading = true;
      const file = event.target.files[0];
      papa.parse(file, {
        delimiter: "",
        newline: "",
        quoteChar: '"',
        escapeChar: '"',
        header: true,
        dynamicTyping: true,
        preview: 0,
        encoding: "",
        worker: true,
        comments: false,
        skipEmptyLines: false,
        error: error => {
          this.errorMsg = "Please Check Your CSV File for the proper format.";
          this.isError = true;
          this.loading = false;
          return;
        },
        complete: results => {
          if (results.errors.length > 0) {
            this.errorMsg = "Please Check Your CSV File for the proper format.";
            this.isError = true;
            this.loading = false;
            return;
          }
          this.loading = false;
          this.submitData(results.data);
          return;
        }
      });
    },
    submitData(data) {
      this.loading = true;
      let url = "http://localhost:5000/upload";
      this.exportJSON.Upload_Array = data;
      let exportData = JSON.stringify(this.exportJSON.Upload_Array);
      console.log(exportData);
      // Specify json in headers otherwise flask API will drop all data associated will POST request
      axios
        .post(url, exportData, {
          headers: {
            "Content-Type": "application/json"
          }
        })
        .then(response => {
          console.log(response);
        })
        .catch(() => {
          this.loading = false;
          this.isError = true;
        });
      this.loading = false;
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
