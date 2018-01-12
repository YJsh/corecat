<template>
  <div>

    <nav class="navbar navbar-default navbar-fixed-top">
      <div class="container-fluid">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
          <a class="navbar-brand" href="#">
            <img alt="Brand" src="../assets/logo.png">
          </a>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
          <ul class="nav navbar-nav">
            <li class="active"><a href="#">Link <span class="sr-only">(current)</span></a></li>
          </ul>

          <ul class="nav navbar-nav navbar-right">
            <el-button type="info" size="medium" v-on:click="logout" plain>退出登录</el-button>
            <!--<button>xxxx</button>-->
          </ul>
        </div><!-- /.navbar-collapse -->
      </div><!-- /.container-fluid -->
    </nav>

  </div>
</template>

<script>
  import bootstrap from "bootstrap"
  import "bootstrap/dist/css/bootstrap.min.css"
  import ElButton from "element-ui/packages/button/src/button";
  import { logout } from "../api";

  export default {
    components: {ElButton},
    name: "nav-menu",
    methods: {
      logout() {
        console.log("logout");
        logout().then(this.afterLogout);
      },
      afterLogout(response) {
        this.$cookie.delete("token");
        this.$router.push("/login");
      }
    }
  }
</script>

<style scoped>
  .el-button {
    margin-top: 8%;
    margin-bottom: 8%;
  }
</style>
