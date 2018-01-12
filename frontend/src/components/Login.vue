<template>
  <div id="login">
    <el-carousel height="100%">
      <el-carousel-item v-for="item in 4" :key="item">
        <h3>{{ item }}</h3>
      </el-carousel-item>
    </el-carousel>

    <el-input type="password" placeholder="请输入密码" v-model="password" @keyup.enter.native="login" clearable>
    </el-input>
  </div>
</template>

<script>
  import Vue from "vue"
  import { Carousel, CarouselItem, Input } from "element-ui"
  import "element-ui/lib/theme-chalk/index.css"
  import { login } from "../api";

  Vue.use(Carousel);
  Vue.use(CarouselItem);
  Vue.use(Input);

  export default {
    name: "login",
    data: function() {
      return {
        password: "",
      }
    },
    methods: {
      login: function() {
        login(this.password).then(this.afterLogin);
      },
      afterLogin(response) {
        if (response.status === 200) {
          this.$router.push("/");
        }
      },
    }
  }
</script>

<style scoped>
  div #login, .el-carousel {
    height: 100%;
  }

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
    width: 320px;
    position:absolute;
    left: 60%;
    top: 40%;
    z-index: 2;
  }
</style>
