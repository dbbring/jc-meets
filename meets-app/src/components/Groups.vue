<template>
  <div id="groups">
    <div class="row">
      <!-- Error block for exceptions -->
      <div v-if="isError" class="col-sm-12 text-center mt-5">
        <h5 class="h5 text-danger">There was a Error Submitting Your Request.</h5>
      </div>
      <!-- Loader -->
      <div v-else-if="loading" class="col-sm-12 text-center mt-5">
        <img src="svg_loader.svg" height="150">
      </div>
      <!-- Main Content Block -->
      <div v-else v-for="(x, index) in groups" :key="index" class="col-lg-6">
        <div class="card text-center mt-3">
          <div class="card-header">Standard Group</div>
          <div class="card-body">
            <h5 class="card-title">{{ x.Group_Name }}</h5>
            <p class="card-text">Group Description would go here normally..</p>
            <a href="#" class="btn btn-primary" @click="showGroupDetails(index)">Group Details</a>
          </div>
          <div class="card-footer text-muted">
            <i class="fas fa-plus-circle mr-2" @click="showAddModal = true" title="Add a New Group"></i>
            <i class="fas fa-edit" @click="editModal(index)" title="Edit Group"></i>
            <i class="fas fa-trash-alt ml-2" @click="deleteModal(index)" title="Delete Group"></i>
          </div>
        </div>
        <!-- end card -->
      </div>
    </div>
    <!--========================= Modals ================================================ -->
    <!-- Edit Modal -->
    <modal v-if="showEditModal" @close="showEditModal = false">
      <h3 slot="header">Edit Group</h3>
      <div slot="body">
        <form class="form">
          <label class="label small text-left">Group Name:</label>
          <input type="text" v-model="editName">
        </form>
      </div>
      <div slot="footer">
        <button type="button" class="btn btn-secondary" @click="showEditModal = false">Cancel</button>
        <button type="button" class="btn btn-success" @click="submitEditModal()">Ok</button>
      </div>
    </modal>
    <!-- Delete Modal -->
    <modal v-if="showDeleteModal" @close="showDeleteModal = false">
      <h3 slot="header">Delete Group</h3>
      <div slot="body">Are you sure you want to delete this group?</div>
      <div slot="footer">
        <button type="button" class="btn btn-secondary" @click="showDeleteModal = false">Cancel</button>
        <button type="button" class="btn btn-success" @click="submitDeleteModal()">Ok</button>
      </div>
    </modal>
    <!-- Add new group modal -->
    <modal v-if="showAddModal" @close="showAddModal = false">
      <h3 slot="header">Add New Group</h3>
      <div slot="body">
        <form class="form">
          <label class="label small text-left">Group Name:</label>
          <input type="text" v-model="addName">
        </form>
      </div>
      <div slot="footer">
        <button type="button" class="btn btn-secondary" @click="showAddModal = false">Cancel</button>
        <button type="button" class="btn btn-success" @click="submitAddModal()">Ok</button>
      </div>
    </modal>
    <!-- Show Group details modal -->
    <modal v-if="showDetailModal" @close="showDetailModal = false">
      <h3 slot="header">{{ groupDetails.groupName }}</h3>
      <div slot="body">
        Organizer:
        <div v-for="(x, index) in groupDetails.groupManagers" :key="index">{{ x }}</div>
        <br>
        <br>Presenters:
        <div v-for="(x, index) in groupDetails.groupPresenters" :key="index + 200">{{ x }}</div>
        <br>
        <br>Members:
        <div v-for="(x, index) in groupDetails.groupMembers" :key="index + 100">{{ x }}</div>
      </div>
      <div slot="footer">
        <button type="button" class="btn btn-success" @click="showDetailModal = false">Ok</button>
      </div>
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
      users: [],
      roles: [],
      memebershipRoles: [],
      showEditModal: false,
      showDeleteModal: false,
      showAddModal: false,
      showDetailModal: false,
      editName: null,
      addName: null,
      groupDetails: {
        groupName: null,
        groupMembers: [],
        groupManagers: [],
        groupPresenters: []
      },
      isError: false
    };
  },
  methods: {
    /*
    @params -> None
    @return -> Json array of group data
    */
    getData() {
      axios
        .get("http://localhost:5000/group")
        .then(response => {
          this.groups = response.data;
          this.loading = false;
        })
        .catch(() => {
          this.loading = false;
          this.isError = true;
        });
    },
    /*
    @params -> int, index number of selected group item
    @return -> none
    */
    deleteModal(arrIndexNum) {
      this.activeGroup = arrIndexNum;
      this.showDeleteModal = true;
    },
    /*
    @params -> None.
    @return -> None.
    */
    submitDeleteModal() {
      this.showDeleteModal = false;
      this.loading = true;
      let url =
        "http://localhost:5000/group/" +
        this.groups[this.activeGroup].Group_Name;
      // Encode URL, odds are we are going to have spaces
      url = encodeURI(url);
      axios
        .delete(url)
        .then(() => {
          this.getData();
        })
        .catch(() => {
          this.loading = false;
          this.isError = true;
        });
    },
    /*
    @params -> int, index number of selected group item
    @return -> none
    */
    editModal(arrIndexNum) {
      this.activeGroup = arrIndexNum;
      this.showEditModal = true;
      this.editName = this.groups[arrIndexNum].Group_Name;
    },
    /*
    @params -> None.
    @return -> None.
    */
    submitEditModal() {
      this.showEditModal = false;
      this.loading = true;
      let cleanEditName = this.sanitize(this.editName);
      let url = "http://localhost:5000/group";
      let data = JSON.stringify({
        // Add one to the active group variable because arrays are zero based in JS and SQLITE is NOT 0 based
        Group_ID: this.activeGroup + 1,
        Group_Name: cleanEditName
      });
      axios
        .put(url, data, {
          headers: {
            "Content-Type": "application/json"
          }
        })
        .then(() => {
          this.loading = false;
          // Instead of making another API call lets just update the current array
          this.groups[this.activeGroup].Group_Name = this.editName;
        });
    },
    /*
    @params -> int, index number of selected group item
    @return -> none
    */
    submitAddModal() {
      this.showAddModal = false;
      this.loading = true;
      let cleanAddName = this.sanitize(this.addName);
      let url = "http://localhost:5000/group";
      let data = JSON.stringify({
        Group_Name: cleanAddName
      });
      // Specify json in headers otherwise flask API will drop all data associated will POST request
      axios
        .post(url, data, {
          headers: {
            "Content-Type": "application/json"
          }
        })
        .then(() => {
          this.getData();
        })
        .catch(() => {
          this.loading = false;
          this.isError = true;
        });
    },
    /*
    @params -> int, index number of selected group item
    @return -> none
    */
    // ============== TODO - break this method down to much smaller methods and not use so many loops.
    showGroupDetails(arrIndexNum) {
      // Clear out our bound variables
      this.groupDetails.groupMembers = [];
      this.groupDetails.groupManagers = [];
      this.groupDetails.groupPresenters = [];
      this.showDetailModal = true;
      this.groupDetails.groupName = this.groups[arrIndexNum].Group_Name;
      // Filter our array down to just the selected group
      let filteredGroupArray = this.memebershipRoles.filter(filterByGroup);
      //Iterate through all users to find what each role of the group is.
      // I could have done a sub-query SQL API end point as well, but I prefer to do the data maniuplation on the front end
      // leaving the back end more flexible to suit everyone needs
      for (let x = 0; x < this.users.length; x++) {
        // Find the Members of the group
        for (let z = 0; z < filteredGroupArray.length; z++) {
          if (
            this.users[x].User_ID === filteredGroupArray[z].Member_User_ID &&
            filteredGroupArray[z].Member_Role_ID === 2
          ) {
            this.groupDetails.groupMembers.push(
              this.users[x].User_First_Name + " " + this.users[x].User_Last_Name
            );
            // Find the Organizers of the group
          } else if (
            this.users[x].User_ID === filteredGroupArray[z].Member_User_ID &&
            filteredGroupArray[z].Member_Role_ID === 3
          ) {
            this.groupDetails.groupManagers.push(
              this.users[x].User_First_Name + " " + this.users[x].User_Last_Name
            );
            // Find the Presenters of the group
          } else if (
            this.users[x].User_ID === filteredGroupArray[z].Member_User_ID &&
            filteredGroupArray[z].Member_Role_ID === 1
          ) {
            this.groupDetails.groupPresenters.push(
              this.users[x].User_First_Name + " " + this.users[x].User_Last_Name
            );
          }
        }
      }
      /*
    @params -> Group Object, must have Member_Group_ID prop
    @return -> Object that is equal to the group id
    */
      function filterByGroup(groupObj) {
        return groupObj.Member_Group_ID === arrIndexNum + 1;
      }
    },
    // Clean data in , Clean data out
    sanitize(input) {
      return input
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
    }
  },
  // TODO clean up mounted function with custom axios functions. DRY....DRY...
  mounted() {
    axios
      .get("http://localhost:5000/user")
      .then(response => {
        this.users = response.data;
      })
      .catch(() => {
        this.loading = false;
        this.isError = true;
      });
    axios
      .get("http://localhost:5000/role")
      .then(response => {
        this.roles = response.data;
      })
      .catch(() => {
        this.loading = false;
        this.isError = true;
      });
    axios
      .get("http://localhost:5000/member")
      .then(response => {
        this.memebershipRoles = response.data;
      })
      .catch(() => {
        this.loading = false;
        this.isError = true;
      });
    // Loading SVG gets taken down inside getData() method
    this.getData();
  }
};
</script>

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
