<script src="../main.js"></script>
<template>
  <div>
    <el-carousel indicator-position="outside">
      <el-carousel-item v-for="item in 4" :key="item">
        <h3>{{ item }}</h3>
      </el-carousel-item>
    </el-carousel>

    <el-input type="password" placeholder="请输入密码" v-model="pwd" @keyup.enter.native="login" clearable>
    </el-input>
  </div>
</template>

<script>
  import Vue from "vue"
  import { Carousel, CarouselItem, Input } from "element-ui"
  import "element-ui/lib/theme-chalk/index.css"

  Vue.use(Carousel);
  Vue.use(CarouselItem);
  Vue.use(Input);

  export default {
    name: "login",
    data: function() {
      return {
        pwd: "",
      }
    },
    mounted: function() {

    },
    methods: {
      login: function() {
        console.log(this.pwd);
      }
    }
  }
</script>

<style scoped>
  .el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 300px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }

  .el-input {
    width: 280px;
    position:absolute;
    left: 60%;
    top: 40%;
    z-index: 2;
  }
</style>
