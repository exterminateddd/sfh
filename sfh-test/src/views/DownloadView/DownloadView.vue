<template>
    <div class="container download-container">
        <h1>{{ $route.params.code }}</h1>
        <img src="./../../assets/spinner.gif" alt="Loading" style="width: 72px;" :class="{opacity0: isCheckFinished}">
        <h2 v-if="fileExists">{{ $root.l('fileFound') }}</h2>
        <h2 v-if="fileExists">{{ timeUntilExpiration.getHours() }}h {{ timeUntilExpiration.getMinutes() }}m {{ timeUntilExpiration.getSeconds() }}s</h2>
        <h2 v-else-if="isCheckFinished">{{ $root.l('fileNotFound') }}</h2>
        <input type="button" :value="$root.l('attemptDownload')" @click="attemptDownload" id="check-button" v-if="fileExists">
    </div>
    
</template>
<script>
import '../../assets/global.css';
import axiosClient from '@/axiosClient.js';

export default {
    data() {
        return {
            isCheckFinished: false,
            fileExists: false,
            expirationTimestamp: new Date(0),
            timeUntilExpiration: new Date(0)
        }
    },
    methods: {
        checkIfFileExists() {
            axiosClient.get('/check_if_file_exists/'+this.$route.params.code).then((resp) => {
                this.isCheckFinished = true;
                this.fileExists = resp.data.result;
                this.expirationTimestamp = new Date(resp.data.expires_at*1000);
                if (this.fileExists) {
                    this.updateTime()
                }
            }).catch(() => {})
        },
        attemptDownload() {
            if (!this.fileExists) {
                return
            }
            axiosClient.get('/download_file/'+this.$route.params.code,
                {
                    responseType: 'blob'
                }).then((resp) => {
                    let blob = resp.data

                    let virtualLink = document.createElement('a');
                    virtualLink.href = window.URL.createObjectURL(blob);

                    const contentDisposition = resp.headers['content-disposition'];

                    const filename = contentDisposition.substring(contentDisposition.indexOf('filename=') + 9, contentDisposition.length);
                    virtualLink.download = filename;
                    virtualLink.target = '_blank';
                    virtualLink.click();
                    window.URL.revokeObjectURL(virtualLink.href)

            }).catch(() => {})
        },
        updateTime() {
            let currentDate = new Date();
            let currentTimeDelta = new Date(this.expirationTimestamp.getTime()-currentDate.getTime());
            currentTimeDelta.setTime(currentTimeDelta.getTime() + currentDate.getTimezoneOffset()*60000)
            let timeLeft = currentTimeDelta.getTime()/1000 - currentDate.getTimezoneOffset()*60;
            if (timeLeft < 0) {
                this.fileExists = false;
            }
            this.timeUntilExpiration = currentTimeDelta;
        }
    },
    created() {
        this.checkIfFileExists();
        setInterval(this.updateTime, 1000)
    }
}
</script>
<style scoped>
@import url('./DownloadView.css');
</style>