<template>
  <div :class="`qp-card ${bgColor}`" :style="`${bgColor}`">
    <div class="qp-card-main">
        <slot />
    </div>
  </div>
</template>

<script>
    export default {
        name: "qpCard",
        props: {
            color: {
                type: String,
                default: "base"
            }
        },
        computed: {
            bgColor () {
                if (this.color != "base") {
                    return `qp-card-bg-${this.color}`
                }
                return ""
            }
        }
    }
</script>

<style scoped>
    .qp-card {
        background-color: var(--qp-base);
        color: var(--qp-base);
        border-radius: 4px;
        box-shadow: 0 0 3px rgba(67, 82, 89, 0.04);
    }
    .qp-card.qp-card-bg-primary {
        background-color: var(--qp-primary);
        color: var(--qp-base);
    }
    .qp-card-main {
        padding: 20px;
    }
</style>
