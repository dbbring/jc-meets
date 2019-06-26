<template>
  <div id="groups">
    <div class="row">
      <div v-if="loading" class="col-sm-12 text-center mt-5">
        <img src="../../static/images/svg_loader.svg" height="150">
      </div>
      <div v-else v-for="(x, index) in groups" :key="index" class="col-lg-6">
        <div class="card text-center mt-3">
          <div class="card-header">Standard Group</div>
          <div class="card-body">
            <h5 class="card-title">{{x.Group_Name}}</h5>
            <p class="card-text">Group Description would go here normally..</p>
            <a href="#" class="btn btn-primary">Join Group</a>
          </div>
          <div class="card-footer text-muted">
            <i class="fas fa-plus-circle mr-2" @click="showAddModal = true" title="Add a New Group"></i>
            <i class="fas fa-edit" @click="editModal(index)" title="Edit Group"></i>
            <i class="fas fa-trash-alt ml-2" @click="showDeleteModal = true" title="Delete Group"></i>
          </div>
        </div>
        <!-- end card -->
      </div>
    </div>
    <modal v-if="showEditModal" @close="showEditModal = false">
      <h3 slot="header">Edit Group</h3>
      <div slot="body">
        <form class="form">
          <input type="text" v-model="editName">
        </form>
      </div>
      <div slot="footer">
        <button type="button" class="btn btn-secondary" @click="showEditModal = false">Cancel</button>
        <button type="button" class="btn btn-success" @click="submitEditModal()">Ok</button>
      </div>
    </modal>
    <modal v-if="showDeleteModal" @close="showDeleteModal = false">
      <h3 slot="header">Delete Group</h3>
      <div slot="body">Are you sure you want to delete this group?</div>
    </modal>
    <modal v-if="showAddModal" @close="showAddModal = false">
      <h3 slot="header">New Group</h3>
      <div slot="body">New Group Form here</div>
    </modal>
  </div>
</template>

<script>
import axios from "axios";
import Modal from "./Modal";

export default {
  name: "groups",
  components: { Modal },
  data() {
    return {
      loading: true,
      activeGroup: null,
      groups: [],
      showEditModal: false,
      showDeleteModal: false,
      showAddModal: false,
      editName: "test"
    };
  },
  methods: {
    getData() {
      axios.get("http://localhost:5000/group").then(response => {
        this.groups = response.data;
        this.loading = false;
      });
    },
    editModal(arrIndexNum) {
      this.activeGroup = arrIndexNum;
      this.showEditModal = true;
      this.editName = this.groups[arrIndexNum].Group_Name;
    },
    submitEditModal() {
      this.showEditModal = false;
      this.loading = true;
      let url = "http://localhost:5000/group";
      let data = JSON.stringify({
        Group_ID: this.activeGroup + 1,
        Group_Name: this.editName
      });
      axios
        .put(url, data, {
          headers: {
            "Content-Type": "application/json"
          }
        })
        .then(response => {
          this.loading = false;
          this.groups[this.activeGroup].Group_Name = this.editName;
        });
    }
  },
  mounted() {
    this.getData();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
i {
  cursor: pointer;
  font-size: 1.25rem;
  transition: all 0.5s;
}
i:hover {
  color: red;
}
</style>
