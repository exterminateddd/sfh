import { createApp } from 'vue';
import App from './App.vue';
import MainView from './views/MainView/MainView.vue';
import UploadView from './views/UploadView/UploadView.vue';
import DownloadView from './views/DownloadView/DownloadView.vue';
import ErrorView from './views/ErrorView/ErrorView.vue';
import GuideView from './views/GuideView/GuideView.vue';
import {createRouter, createWebHistory} from 'vue-router';

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'main',
            component: MainView
        },
        {
            path: '/upload',
            name: 'upload',
            component: UploadView
        },
        {
            path: '/download/:code',
            name: 'download',
            sensitive: false,
            component: DownloadView
        },
        {
            path: '/error',
            name: 'error',
            component: ErrorView,
            props: route => ({ errorText: route.query.text })
        },
        {
            path: '/guide',
            name: 'guide',
            component: GuideView
        }
    ]
})

createApp(App).use(router).mount('#app')
