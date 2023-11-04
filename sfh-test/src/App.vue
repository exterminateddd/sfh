<template>
  <div class="app-container">
    <header>
      <h1 class="header-title" @click="$router.push({'name': 'main'})">SFH</h1>
      <select id="locale-select" v-model="locale">
        <option value="EN">{{ l('EN') }}</option>
        <option value="RU">{{ l('RU') }}</option>
      </select>
    </header>
    <router-view></router-view>
    <footer>
      <h1 class="footer-guide-link" @click="$router.push({'name': 'guide'})" v-if="['main'].includes($route.name)">{{ l('guide') }}</h1>
      <h1>{{ appVersion }}</h1>
    </footer>
  </div>
  
</template>

<script>
import {RouterView} from 'vue-router';
import './assets/global.css';
import packageJson from './../package.json';

export default {
  name: 'App',
  data() {
    return {
      locale: 'RU'
    }
  },
  computed: {
    appVersion() {
      return packageJson ? packageJson.version : '1.0.0';
    }
  },
  methods: {
    l(translationCode) {
      const localeJson = require('./locales/'+this.locale+'.json');
      return !(translationCode in localeJson) ? '#'+translationCode : localeJson[translationCode];
    },
    error(errorText, errorCode) {
      this.$router.push({ name: 'error', query: { text: errorText, code: errorCode } })
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
  height: 100%;
}
.footer-guide-link {
  cursor: pointer;
}
.footer-guide-link:hover, .footer-guide-link:focus {
  text-decoration: underline;
}
header, footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-right: 18px;
}
footer {
  padding: 0 8px;
}
footer * {
  font-size: 22px;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100vh;
}
</style>
