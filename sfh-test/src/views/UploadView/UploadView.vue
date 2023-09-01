<template>
    <div class="container upload-container">
        <form class="upload-form" @submit="uploadFormSubmitHandler">
            <input type="file" name="" id="file-input" style="display: none!important;" @change="fileInputChangeHandler">
            <label for="file-input" :class="{'bg-green': uploadedFile}">
                <h3>{{ !uploadedFile ? $root.l('uploadAFile') : $root.l('fileSelected') }}</h3>
                <h4 style="color: red" :class="{'green-text': uploadedFile!==undefined, 'filename': true}">
                    {{ uploadedFile ? uploadedFile.name : $root.l('noFileUploaded') }}
                </h4>
            </label>
            <div class="lifetime-select-container">
                <label for="fileLifetime">{{ $root.l('fileLifetime') }}</label>
                <select id="fileLifetime" v-model="fileLifetime">
                    <option value="30">30 {{ $root.l('secs') }}</option>
                    <option value="60">1 {{ $root.l('min') }}</option>
                    <option value="300">5 {{ $root.l('mins') }}</option>
                    <option value="600">10 {{ $root.l('mins') }}</option>
                    <option value="1800">30 {{ $root.l('mins') }}</option>
                    <option value="3600">1 {{ $root.l('hour') }}</option>
                    <option value="43200">12 {{ $root.l('hours2') }}</option>
                </select>
            </div>
            <input type="submit" :value="$root.l('attemptUpload')" :class="{'attempt-upload-button': true, 'button-unclickable': !uploadedFile}" :disabled="!uploadedFile">
        </form>
        <div :class="{'render-after-complete': true, opacity0: !uploadToServerCompleted}">
            <h1 id="filecode">{{ filecode }}</h1>
            <input type="button" :value="$root.l('toDownloadPage')"
                @click="$router.push({ name: 'download', params: {'code': this.filecode} })"
                :class="{'redirect-button': true, 'display-none': !uploadToServerCompleted}">
                <input type="button" :value="$root.l('copyCode')"
                @click="attemptCodeCopy()"
                :class="{'copy-button': true, 'display-none': !uploadToServerCompleted}">
        </div>
    </div>
</template>
<script>
import '../../assets/global.css';
import axiosClient from '@/axiosClient.js';

export default {
    data() {
        return {
            uploadedFile: undefined,
            uploadToServerCompleted: false,
            fileLifetime: 600,
            filecode: '?/?/?/'
        }
    },
    methods: {
        fileInputChangeHandler(e) {
            this.uploadedFile = e.target.files[0];
        },
        attemptFileUpload() {
            if (!this.uploadedFile || !this.fileLifetime) {
                return
            }
            const formData = new FormData();
            formData.append("file", this.uploadedFile);
            formData.append("lifetime", this.fileLifetime);
            process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0';
            axiosClient.post("/upload_file", formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }).then((resp) => {
                this.uploadToServerCompleted = true;
                this.filecode = resp.data;
            }).catch((err) => {
                this.$root.error(err.message);
            });
        },
        uploadFormSubmitHandler(e) {
            e.preventDefault();
            this.attemptFileUpload();
        },
        attemptCodeCopy() {
            alert("doesn't work yet")   
        }
    }
}
</script>
<style scoped>
@import url('./UploadView.css');
</style>