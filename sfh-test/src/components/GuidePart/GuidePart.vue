<template>
    <div class="container" :class="{'container': True, 'reverse': reverse, 'guide-part-container': true}">
        <div :class="{'part-left': true}">
            {{ number }}
        </div>
        <div :class="{'part-right': true, 'clickable': link}" @click="link ? $router.push({ name: link }) : ()=>{}">
            <p>{{ text }}</p>
        </div>
    </div>
</template>
<script>
export default {
    name: 'GuidePart',
    data() {
        return {
            
        }
    },
    props: {
        number: {
            type: Number
        },
        text: {
            type: String
        },
        reverse: {
            type: Boolean,
            default: false,
            required: false
        },
        link: {

        }
    }
}
</script>
<style scoped>
@import url('./GuidePart.css');
</style>