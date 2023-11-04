<template>
    <div class="container guide-container">
        <div class="guide-header">
            <p class="guide-header-title">{{ $root.l('guideHeader') }}</p>
            <p class="guide-header-sub">{{ $root.l('guideHeaderSub') }}</p>
        </div>
        <div class="guide-body">
            <div class="par" v-for="(text, i) in texts" :key="i">
                <guide-part :number="i+1" :text="$root.l(text)" :reverse="i%2===1" :link="links[i]"></guide-part>
            </div>
        </div>
    </div>
</template>
<script>
import '../../assets/global.css';
import './GuideView.css';
import GuidePart from '../../components/GuidePart/GuidePart.vue';

export default {
    data() {
        return {
            texts: [
                'guide1',
                'guide2',
                'guide3',
                'guide4'
            ],
            links: [
                "upload",
                "",
                "",
                ""
            ]
        }
    },
    components: {
        GuidePart
    }
}
</script>