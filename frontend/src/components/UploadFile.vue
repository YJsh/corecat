<template>
  <el-upload
    class="upload-demo"
    name="uploadFile"
    drag
    action="http://localhost:8000/share/addFile"
    ref="upload"
    :on-success="uploadSucc">
    <i class="el-icon-upload"></i>
    <div class="el-upload__text">将文件拖入框内，或<em>点击上传</em></div>
  </el-upload>
</template>

<script>
  import Vue from "vue"
  import { Upload } from "element-ui"
  import "element-ui/lib/theme-chalk/index.css"

  Vue.use(Upload);

  export default {
    name: "upload-file",
    methods: {
      uploadSucc(response, file, fileList) {
        this.$refs.upload.clearFiles();
        this.$store.commit("addNodes", {
          nodeId:response["id"], fileUrl:response["fileUrl"], name:file.name});
      }
    }
  }
</script>

<style scoped>

</style>
