<template>
  <div :class="`qp-card ${isClickable} ${isOverflow} ${bgColor}`" :style="`${height}${marginBottom}`">
    <div class="qp-card-main">
        <slot />
    </div>
  </div>
</template>

<script>
    export default {
        name: "qpCard",
        props: {
            clickable: {
                type: Boolean,
                default: false
            },
            overflow: {
                type: Boolean,
                default: false
            },
            bgcolor: {
                type: String,
                default: "base"
            },
            h: {
                type: String,
                default: ""
            },
            mb: {
                type: String,
                default: ""
            }
        },
        computed: {
            isClickable () {
                return (this.clickable ? "qp-card-clickable" : "")
            },
            isOverflow () {
                return (this.overflow ? "qp-card-overflow" : "")
            },
            bgColor () {
                if (this.bgcolor != "base") {
                    return `qp-card-bg-${this.bgcolor}`
                }
                return ""
            },
            height () {
                return (this.h ? `height:${this.h};` : "")
            },
            marginBottom () {
                return (this.mb ? `margin-bottom:${this.mb};` : "")
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
        transition: box-shadow 0.3s, opacity 0.3s;
    }
    .qp-card.qp-card-clickable:hover {
        box-shadow: 0 0 6px rgba(67, 82, 89, 0.6);
        cursor: pointer;
        opacity: 0.8;
    }
    .qp-card.qp-card-overflow {
        overflow: visible;
    }
    .qp-card.qp-card-bg-primary {
        background-color: var(--qp-primary);
        color: var(--qp-base);
    }
    .qp-card-main {
        padding: 20px;
    }
</style>
