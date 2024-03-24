<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Sidebar from './components/Sidebar.vue';
import MainContentView from './views/MainContentView.vue';
</script>

<template>
  <div id="app">
    <div class="container">
      <Sidebar/>
      <MainContentView />
    </div>
  </div>
  <!-- <RouterView /> -->
</template>

<style scoped>
#app {
  display: flex;
  justify-content: flex-start;
  align-items: stretch; 
  height: 100vh;
}

.container {
  display: flex;
  flex-direction: row;
  width: 100%;
}
</style>
