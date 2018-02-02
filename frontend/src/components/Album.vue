<template>
  <!--<div>-->
    <!--<el-dialog :visible.sync="dialogVisible" size="tiny">-->
      <!--<img width="100%" :src="dialogImageUrl" alt="">-->
    <!--</el-dialog>-->
    <!--<el-upload-->
      <!--action="https://jsonplaceholder.typicode.com/posts/"-->
      <!--list-type="picture-card"-->
      <!--:on-preview="handlePictureCardPreview"-->
      <!--:on-remove="handleRemove">-->
      <!--<i class="el-icon-plus"></i>-->
    <!--</el-upload>-->
  <!--</div>-->
    <el-container>
      <el-main>

      </el-main>
      <el-footer height="250px">
        <p>sss</p>
        <img style="height:200px; width:100px" src="../assets/logo.png">
        <img src="../assets/logo.png">
        <img style="height:200px; width:100px" src="../assets/logo.png">
        <!--<img src="../assets/logo.png">-->

      </el-footer>
    </el-container>
</template>

<script>
  import Vue from "vue"
  import { Dialog, Upload } from "element-ui"
  import ElContainer from "element-ui/packages/container/src/main";
  import ElMain from "element-ui/packages/main/src/main";
  import ElFooter from "element-ui/packages/footer/src/main";

  Vue.use(Dialog);
  Vue.use(Upload);

  export default {
    components: {
      ElFooter,
      ElMain,
      ElContainer},
    name: "album",
    data() {
      return {
        dialogImageUrl: '',
        dialogVisible: false
      };
    },
    methods: {
      handleRemove(file, fileList) {
        console.log(file, fileList);
      },
      handlePictureCardPreview(file) {
        this.dialogImageUrl = file.url;
        this.dialogVisible = true;
      }
    }
  }
</script>

<style scoped>
  .el-container {
    height: 100%;
  }

  img {
    margin-left: 10px;
  }
</style>
