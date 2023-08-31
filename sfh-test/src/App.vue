<template>
  <div class="app-container">
    <header>
      <h1 class="header-title" @click="$router.push({'name': 'main'})">SFH</h1>
      <h1 class="header-guide-link" @click="$router.push({'name': 'guide'})">{{ l('guide') }}</h1>
      <select id="locale-select" v-model="locale">
        <option value="EN">{{ l('EN') }}</option>
        <option value="RU">{{ l('RU') }}</option>
      </select>
    </header>
    <router-view></router-view>
  </div>
  
</template>

<script>
import {RouterView} from 'vue-router';
import './assets/global.css';

export default {
  name: 'App',
  data() {
    return {
      locale: 'RU'
    }
  },
  methods: {
    l(translationCode) {
      const localeJson = require('./locales/'+this.locale+'.json');
      return !(translationCode in localeJson) ? '#'+translationCode : localeJson[translationCode];
    },
    error(errorText) {
      this.$router.push({ name: 'error', query: { text: errorText } })
    }
  },
  components: {
    RouterView
  }
}
</script>

<style>
#locale-select {
  height: 32px;
}
.header-title {
  width: 96px; 
  display: inline-block; color: 
  rgba(255, 0, 76, 0.842); 
  cursor: pointer;
}
.app-container {
  display: flex;
  flex-direction: column;
}
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-right: 18px;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
