<template>
  <div :class="`qp-card ${bgColor} ${isOverflow}`">
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
            },
            overflow: {
                type: Boolean,
                default: false
            }
        },
        computed: {
            bgColor () {
                if (this.color != "base") {
                    return `qp-card-bg-${this.color}`
                }
                return ""
            },
            isOverflow () {
                return (this.overflow ? "qp-card-overflow" : "")
            }
        }
    }
</script>

<style scoped>
    .qp-card {
        background-color: var(--qp-base);
        color: var(--qp-primary);
        border-radius: 4px;
        box-shadow: 0 0 3px rgba(67, 82, 89, 0.04);
        overflow: hidden;
        height: 100%;
    }
    .qp-card.qp-card-bg-primary {
        background-color: var(--qp-primary);
        color: var(--qp-base);
    }
    .qp-card.qp-card-overflow {
        overflow: visible;
    }
    .qp-card-main {
        padding: 20px;
    }
</style>
