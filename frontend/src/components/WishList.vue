<template>
  <div>
    <h3>Hello World</h3>
    <extensible-item></extensible-item>
  </div>
</template>

<script>
  import Vue from "vue"
  import { Table, TableColumn } from "element-ui"
  import ExtensibleItem from "./ExtensibleItem"

  Vue.use(Table);
  Vue.use(TableColumn);

  export default {
    name: "wish-list",
    components: {
      ExtensibleItem,
    },
    data() {
      return {
      }
    }
  }
</script>

<style scoped>

</style>
