<template>
    <div class="container">
        <h1>
            {{ $props.errorText }}
        </h1>
    </div>
</template>
<script>
import '../../assets/global.css';

export default {
    data() {
        return {

        }
    },
    props: {
        errorText: {
            type: String
        }
    }
}
</script>