<template>
  <div v-if="path === '/login'" id="loginApp">
    <router-view/>
  </div>
  <div v-else id="app">
    <nav-menu></nav-menu>
    <router-view/>
  </div>
</template>

<script>
  import NavMenu from './components/NavMenu';

  export default {
    name: 'app',
    computed: {
      path() {
        return this.$route.path
      },
    },
    components: {
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

html,body,#loginApp {height: 100%;}
</style>
