<template>
    <div id="qp-app-sidebar">
        sidebar
    </div>
</template>

<script>
    export default {
        name: 'qpSidebar'
    }
</script>

<style scoped>
    #qp-app-sidebar {
        background-color: var(--qp-base);
        box-shadow: 0 0 3px rgba(67, 82, 89, 0.04);
        box-sizing: border-box;
        vertical-align: top;
        display: inline-block;
        height: calc(100vh - 64px);
        width: 300px;
    }
    @media (max-width: 1199px) {
        #qp-app-sidebar {
            width: 64px;
        }
    }
</style>
