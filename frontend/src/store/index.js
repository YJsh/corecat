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
    let name = args.name;
    let fileUrl = args.fileUrl;
    state.dirTreeNodeAdded = [{name: name, id: nodeId, fileUrl: fileUrl}];
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
