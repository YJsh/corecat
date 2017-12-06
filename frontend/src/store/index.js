import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

const state = {
  count: 1,
  count2: 2,
  dirTreeNode: [
    {
      name: 'test1', open: true, children: [
        {name: 'test1_1'}, {name: 'test1_2'}
      ]
    },
    {
      name: 'test2', open: true, children: [
        {name: 'test2_1'}, {name: 'test2_2'}
      ]
    }
  ]
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
  // addNode(state) {
  //   state.dirTreeNode = [];
  // }
}

const getters = {
  count:function(state){
    return state.count +=100;
  }
}

export default new Vuex.Store({
  state,
  mutations,
  getters
});