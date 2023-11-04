<template>
    <div class="container error-container">
        <h1 class="error-title">
            <span>{{ $props.errorCode }}</span> {{ $props.errorText }}
        </h1>
        <p class="error-sub">
            {{ $root.l('errorSub') }}
        </p>
    </div>
</template>
<style scoped>
.error-container {
    flex-direction: column;
    align-items: center;
    justify-content: start!important;
}
h1.error-title {
    height: 30%;
}
h1.error-title > span {
    color: red;
}
p.error-sub {
    color: rgba(0, 0, 0, 0.493);
}
</style>
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
        },
        errorCode: {
            type: Number,
            default: 500
        }
    }
}
</script>