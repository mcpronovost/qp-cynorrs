<template>
    <div id="qp-app-smallbar">
        smallbar
    </div>
</template>

<script>
    export default {
        name: 'qpSmallbar'
    }
</script>

<style scoped>
    #qp-app-smallbar {
        background-color: var(--qp-base);
        box-shadow: 0 0 3px rgba(67, 82, 89, 0.04);
        box-sizing: border-box;
        vertical-align: top;
        display: inline-block;
        height: calc(100vh - 64px);
        width: 64px;
    }
</style>
