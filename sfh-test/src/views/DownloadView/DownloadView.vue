<template>
    <div class="container download-container">
        <h1>{{ $route.params.code }}</h1>
        <img src="./../../assets/spinner.gif" alt="Loading" style="width: 72px;" :class="{opacity0: isCheckFinished}">
        <h2 v-if="fileExists">{{ $root.l('fileFound') }}</h2>
        <h2 v-else-if="isCheckFinished">{{ $root.l('fileNotFound') }}</h2>
        <input type="button" :value="$root.l('attemptDownload')" @click="attemptDownload" id="check-button" v-if="fileExists">
    </div>
    
</template>
<script>
import '../../assets/global.css';
import get from 'axios';

export default {
    data() {
        return {
            isCheckFinished: false,
            fileExists: false
        }
    },
    methods: {
        checkIfFileExists() {
            console.log('checking if file with code ' + this.$route.params.code + ' exists')
            get('http://'+process.env.VUE_APP_API_ROOT+':5000'+'/check_if_file_exists/'+this.$route.params.code).then((resp) => {
                this.isCheckFinished = true;
                this.fileExists = resp.data.result;
            }).catch(() => {})
        },
        attemptDownload() {
            if (!this.fileExists) {
                return
            }
            get('http://'+process.env.VUE_APP_API_ROOT+':5000'+'/download_file/'+this.$route.params.code).then((resp) => {
                let virtualLink = document.createElement('a');
                virtualLink.href = window.URL.createObjectURL(new Blob([resp.data]));
                const contentDisposition = resp.headers['content-disposition'];
                const filename = contentDisposition.substring(contentDisposition.indexOf('filename=') + 9, contentDisposition.length);
                virtualLink.download = filename;
                virtualLink.target = '_blank';

                virtualLink.click();

            }).catch(() => {})
        }
    },
    mounted() {
        this.checkIfFileExists();
    }
}
</script>
<style scoped>
@import url('./DownloadView.css');
</style>