<template>
  <div v-if="path === '/login'" id="loginApp">
    <router-view/>
  </div>
  <div v-else id="app">
    <nav-menu></nav-menu>
    <el-container>
      <el-aside width="250px">Aside</el-aside>
      <el-main>
        <router-view/>
      </el-main>
    </el-container>
  </div>
</template>

<script>
  import NavMenu from './components/NavMenu';
  import ElContainer from "element-ui/packages/container/src/main";
  import ElMain from "element-ui/packages/main/src/main";
  import ElAside from "element-ui/packages/aside/src/main";

  export default {
    name: 'app',
    computed: {
      path() {
        return this.$route.path
      },
    },
    components: {
      ElAside,
      ElMain,
      ElContainer,
      NavMenu,
    }
  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    padding-top: 50px;
  }

  .el-aside {
    background-color: #e6dbb6;
  }

  html,body,#loginApp {height: 100%;}

  html,body,#app,.el-container,.el-main {height: 100%;}

</style>
