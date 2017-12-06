<template>
  <div>
    <h3>共享目录</h3>
    <dir-tree></dir-tree>
    <upload-file></upload-file>
  </div>
</template>

<script>
  import DirTree from './DirTree'
  import UploadFile from "./UploadFile";

  export default {
    name: 'shared-dir',
    components: {
      UploadFile,
      DirTree,
    }
  }
</script>

<style scoped>

</style>
