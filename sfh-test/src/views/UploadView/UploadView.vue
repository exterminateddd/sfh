<template>
    <div class="container upload-container">
        <form class="upload-form" @submit="uploadFormSubmitHandler">
            <input type="file" name="" id="file-input" style="display: none!important;" @change="fileInputChangeHandler">
            <label for="file-input">
                <h3>{{ $root.l('uploadAFile') }}</h3>
                <h4 style="color: red" :class="{'green-text': uploadedFile!==undefined, 'filename': true}">
                    {{ uploadedFile ? uploadedFile.name : $root.l('noFileUploaded') }}
                </h4>
            </label>
            <div class="lifetime-select-container">
                <label for="fileLifetime">{{ $root.l('fileLifetime') }}</label>
                <select id="fileLifetime" v-model="fileLifetime">
                    <option value="30">30 {{ $root.l('seconds') }}</option>
                    <option value="60">1 {{ $root.l('minute') }}</option>
                    <option value="300">5 {{ $root.l('minutes') }}</option>
                    <option value="600">10 {{ $root.l('minutes') }}</option>
                    <option value="1800">30 {{ $root.l('minutes') }}</option>
                    <option value="3600">1 {{ $root.l('hour') }}</option>
                    <option value="43200">12 {{ $root.l('hours') }}</option>
                </select>
            </div>
            <input type="submit" :value="$root.l('attemptUpload')" class="attempt-upload-button">
        </form>
        <h1 id="filecode" v-if="uploadToServerCompleted">{{ filecode }}</h1>
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
        }
    }
}
</script>
<style scoped>
@import url('./UploadView.css');
</style>