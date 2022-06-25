<template>
  <div class="qp-card">
    <div class="qp-card-main">
        <slot />
    </div>
  </div>
</template>

<script>
    export default {
        name: 'qpCard'
    }
</script>

<style scoped>
    .qp-card {
        background-color: var(--qp-base);
        border-radius: 4px;
        box-shadow: 0 0 3px rgba(67, 82, 89, 0.04);
    }
    .qp-card-main {
        padding: 20px;
    }
</style>
