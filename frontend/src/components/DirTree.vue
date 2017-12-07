<template>
  <div>
    <ul id="dirTree" class="ztree"></ul>
  </div>
</template>

<script>
  import ztree from 'ztree'
  import 'ztree/css/metroStyle/metroStyle.css'
  // import axios from 'axios'

  export default {
    name: "dir-tree",
    mounted() {
      console.log(this);
      let zTreeObj;
      const setting = {
        // async: {
          // enable: true,
          // type: "post",
          // url: "http://corncat.com:9000/share/"
        // },
        callback: {
          beforeDrop: this.beforeDrop,
          onClick: this.onClick,
          onDrop: this.onDrop,
          onRemove: this.onRemove,
          onRename: this.onRename,
          onRightClick: this.onRightClick,
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
      },
      dirTreeNodeAdded() {
        return this.$store.state.dirTreeNodeAdded;
      },
    },
    watch: {
      dirTreeNodeAdded() {
        let zTreeObj = $.fn.zTree.getZTreeObj("dirTree");
        zTreeObj.addNodes(null, this.dirTreeNodeAdded);
      }
    },
    methods: {
      beforeDrop: function(treeId, treeNodes, targetNode, moveType) {
        if ("inner" === moveType) {
          if (targetNode == null) {
            return false;
          }
        }
        else if (targetNode.parentTId == null) {
          return false;
        }
        return true;
      },
      onClick: function(event, treeId, treeNode){
        console.log("test2");
      },
      onDrop: function(event, treeId, treeNode) {
        console.log(event, treeId, treeNode);
      },
      onRemove: function(event, treeId, treeNode) {

      },
      onRename: function(event, treeId, treeNode, isCancel) {

      },
      onRightClick: function(event, treeId, treeNode) {
      },
    }
  }
</script>

<style scoped>
</style>
