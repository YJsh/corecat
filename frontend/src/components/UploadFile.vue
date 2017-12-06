<template>
  <el-upload
    class="upload-demo"
    drag
    action="https://jsonplaceholder.typicode.com/posts/"
    multiple>
    <i class="el-icon-upload"></i>
    <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
  </el-upload>
</template>

<script>
  import Vue from 'vue'
  import { Upload } from 'element-ui'
  import 'element-ui/lib/theme-chalk/index.css'

  Vue.use(Upload);

  export default {
    name: "upload-file",
  }
</script>

<style scoped>

</style>
