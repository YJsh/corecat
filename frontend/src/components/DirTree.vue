<template>
  <div>
    <ul id="dirTree" class="ztree"></ul>
    <!--<button @click="$store.commit('add')">上传</button>-->
  </div>
</template>

<script>
  import ztree from 'ztree'
  import 'ztree/css/metroStyle/metroStyle.css'

  export default {
    name: "dir-tree",
    mounted() {
      let zTreeObj;
      const setting = {
        // async: {
          // enable: true,
          // type: "post",
          // url: "http://corncat.com:9000/share/"
        // },
        callback: {
          onClick: function(event, treeId, treeNode) {
            console.log(treeId);
            console.log(treeNode);
            // $.post({
            //   data: treeId,
            //   url: 'http://corncat.com:9000/share/download"'
            // })
          },
          onDrop: function(event, treeId, treeNodes, targetNode, moveType) {

          },
          onRemove: function(event, treeId, treeNode) {

          },
          onRename: function(event, treeId, treeNode, isCancel) {

          },
          onRightClick: function(event, treeId, treeNode) {
            console.log(event.target);
            console.log(treeNode)
          },
        },
        data: {
          keep: {
            leaf: true,
            parent: true,
          },
        },
        edit: {
          drag: {
            autoExpandTrigger: false,
          },
          editNameSelectAll: true,
          enable: true,
          removeTitle: '删除',
          renameTitle: '重命名',
          showRemoveBtn: true,
          showRenameBtn: true
        },
        view: {
          autoCancelSelected: false,
          showTitle: false,
        },
      };
      zTreeObj = $.fn.zTree.init($("#dirTree"), setting, this.dirTreeNode);
    },
    computed: {
      dirTreeNode() {
        return this.$store.state.dirTreeNode;
      }
    },
  }
</script>

<style scoped>
</style>
