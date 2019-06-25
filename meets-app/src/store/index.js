/*eslint-disable*/
import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    data: [
      {
        ID: "3471DA17-401F-9633-BF81-4CADA6FD5C79",
        Name: "Kyra Lester",
        Description: "Curabitur dictum. Phasellus in",
        Date: "2017-07-23T04:24:49-07:00",
        Amount: "345.54"
      },
      {
        ID: "9F5C9912-936A-FB85-1EDB-9DA87BE7FF1E",
        Name: "Buckminster Alvarado",
        Description: "dui, in sodales elit erat vitae risus. Duis a mi",
        Date: "2018-11-08T05:44:15-08:00",
        Amount: "677.08"
      }
    ],
    singleItem: {},
    checkedItems: []
  },
  mutations: {
    setSingleItem(state, item) {
      state.singleItem = [];
      state.singleItem = item;
    },
    updateSingeItemInData(state, rowID) {
      state.data[rowID] = state.singleItem;
    },
    updateCheckedItems(state, newCheckedItemsArray) {
      state.checkedItems = newCheckedItemsArray;
    },
    deleteDataItem(state, RowID) {
      state.data.splice(RowID, 1);
    },
    setData(state, newDataArray) {
      state.data = [];
      state.data = newDataArray;
    }
  },
  actions: {
    getSingleItem(context, id) {
      context.commit("setSingleItem", store.state.data[id]);
    },
    deleteDataItems(context) {
      for (let x = 0; x < store.state.checkedItems.length; x++) {
        context.commit("deleteDataItem", store.state.checkedItems[x]);
      }
    }
  }
});

export default store;
