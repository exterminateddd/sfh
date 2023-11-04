<template>
    <div class="container">
        <div class="container-left">
            <div class="download-section">
                <h1> {{ $root.l('downloadAFile') }} </h1>
                <input type="text" class="code-value" maxlength="6" v-model="codeValue" @input="inputChangeHandler" ref="codeInput" :placeholder="$root.l('fileCode')">
                <input type="button" :value="$root.l('proceed')" class="download-button" @click="tryToRedirectToDownload">
            </div>
            <div class="upload-section">
                <h1> {{ $root.l('uploadAFile') }} </h1>
                <router-link to="/upload">
                    <input type="button" :value="$root.l('uploadAFile')" class="upload-button" >
                </router-link>
            </div>
        </div>
        <div class="container-right">
            <sfh-logo></sfh-logo>
        </div>
    </div>
</template>
<script>
import '../../assets/global.css';
import { RouterLink } from 'vue-router';
import sfhLogo from '../../components/sfhLogo/sfhLogo.vue';
export default {
    data() {
        return {
            codeValue: ''
        }
    },
    methods: {
        tryToRedirectToDownload() {
            if (this.codeValue.length==6) {
                this.$router.push({ name: 'download', params: {'code': this.codeValue} })
            }
        },
        inputChangeHandler() {
            this.$refs.codeInput.value = this.codeValue.toUpperCase();
            this.codeValue = this.$refs.codeInput.value;
        }
    },
    components: {
        RouterLink,
        sfhLogo
    }
}
</script>
<style scoped>
@import url('./MainView.css')
</style>
