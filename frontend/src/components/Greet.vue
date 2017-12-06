<template>
  <div>
    <h3> {{ count }}</h3>
    <!--<h3 v-show="false"> {{ count2 }}</h3>-->
    <button @click="$store.commit('add')">+</button>
    <button @click="$store.commit('reduce')">-</button>
  </div>
</template>

<script>
  import store from '@/store'
  // import {mapState} from 'vuex';
  import {mapState,mapMutations,mapGetters} from 'vuex';

  export default {
    name: "greet",
    watch: {
      count2(newVal, oldVal) {
        console.log(newVal, oldVal);
      }
    },
    computed: {
      count() {
        this.test();
        console.log("count");
        return this.$store.getters.count;
      },
      count2() {
        return this.$store.state.count2 + 10;
      }
    },
    methods: {
      test: function () {
        console.log(1);
        store.state.count2 += 1;
      }
    },
  }

</script>

<style scoped>
</style>
