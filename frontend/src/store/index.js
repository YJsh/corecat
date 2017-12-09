import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

const state = {
  count: 1,
  count2: 2,
  dirTreeNodeAdded: [],
};

const mutations={
  add(state){
    state.count+=1;
  },
  addcount2(state) {
    state.count2 -= 1;
  },
  reduce(state){
    state.count-=1;
  },
  addNodes(state, args) {
    let nodeId = args.nodeId;
    let fileList = args.fileList;

    state.dirTreeNodeAdded = [];
    for (let i in fileList) {
      if(fileList.hasOwnProperty(i)) {
        state.dirTreeNodeAdded.push({name: fileList[i]["name"], id: nodeId});
        nodeId += 1;
      }
    }
  }
};

const getters = {
  count:function(state){
    return state.count +=100;
  }
};

export default new Vuex.Store({
  state,
  mutations,
  getters
});
