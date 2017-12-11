<template>
  <div>
    <ul id="dirTree" class="ztree"></ul>
  </div>
</template>

<script>
  import ztree from 'ztree'
  import 'ztree/css/metroStyle/metroStyle.css'
  import { addDir, getDirTree, dropNode, downloadFile, removeNode, renameNode } from '@/api'

  export default {
    name: "dir-tree",
    mounted() {
      const setting = {
        callback: {
          beforeDrop: this.beforeDrop,
          onClick: this.onClick,
          onDrop: this.onDrop,
          onRemove: this.onRemove,
          onRename: this.onRename,
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
          addHoverDom: this.addHoverDom,
          removeHoverDom: this.removeHoverDom,
          autoCancelSelected: false,
          showTitle: false,
        },
      };
      getDirTree().then(function(response) {
        $.fn.zTree.init($("#dirTree"), setting, response.data);
      });
    },
    computed: {
      dirTreeNodeAdded() {
        return this.$store.state.dirTreeNodeAdded;
      },
    },
    watch: {
      dirTreeNodeAdded() {
        let zTreeObj = $.fn.zTree.getZTreeObj("dirTree");
        let root = zTreeObj.getNodeByParam("id", -1, null);
        zTreeObj.addNodes(root, this.dirTreeNodeAdded);
      }
    },
    methods: {
      beforeDrop: function(treeId, treeNodes, targetNode, moveType, isCopy) {
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
        if (treeNode.isParent) {
          let zTreeObj = $.fn.zTree.getZTreeObj("dirTree");
          zTreeObj.expandNode(treeNode);
        }
        else {
          // TODO: 预览
        }
      },
      onDrop: function(event, treeId, treeNodes, targetNode, moveType, isCopy) {
        if (moveType === null) return;

        let nodeIds = [];
        for (let i in treeNodes) {
          if(treeNodes.hasOwnProperty(i)) {
            let node = treeNodes[i];
            nodeIds.push(node.id);
          }
        }
        dropNode(nodeIds, treeNodes[0].getParentNode().id);
      },
      onRemove: function(event, treeId, treeNode) {
        removeNode(treeNode.id);
      },
      onRename: function(event, treeId, treeNode, isCancel) {
        if (isCancel) return;
        renameNode(treeNode.id, treeNode.name);
      },
      addHoverDom: function(treeId, treeNode) {
        // TODO: Hover按钮会触发node的点击事件
        if (treeNode.editNameFlag || $("#downloadBtn_" + treeNode.tId).length>0) return;

        let span = $("#" + treeNode.tId + "_span");
        let addStr = "<span class='button add' id='downloadBtn_" + treeNode.tId
          + "' title='下载' onfocus='this.blur();'></span>";
        span.append(addStr);

        let btn = $("#downloadBtn_" + treeNode.tId);
        if (btn) {
          if (treeNode.isParent) {
            btn.bind("click", function() {
              addDir(treeNode.id, "新建文件夹").then(function(response){
                if (response.status !== 200) return;
                let zTree = $.fn.zTree.getZTreeObj("dirTree");
                zTree.addNodes(treeNode, {id: response.data, isParent: true, name: "新建文件夹"});
                return true;
              });
            });
          }
          else {
            btn.bind("click", function() {
              window.location.href = treeNode.fileUrl;
            });
          }
        }
      },
      removeHoverDom: function(treeId, treeNode) {
        $("#downloadBtn_"+treeNode.tId).unbind().remove();
      },
    }
  }
</script>

<style scoped>

</style>
