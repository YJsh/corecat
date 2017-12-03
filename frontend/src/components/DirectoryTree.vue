<template>
  <div>
    <ul id="dirTree" class="ztree"></ul>
  </div>
</template>

<script>
  import 'ztree'
  import 'ztree/css/metroStyle/metroStyle.css'

  export default {
    name: "directory-tree",
    mounted() {
      let zTreeObj;
      const setting = {};
      const zNodes = [
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
      ];
      zTreeObj = $.fn.zTree.init($("#dirTree"), setting, zNodes);
    }
  }
</script>

<style scoped>
</style>
