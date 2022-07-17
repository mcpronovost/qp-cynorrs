<template>
  <div :class="`qp-card ${isClickable} ${isOverflow} ${bgColor}`" :style="`${height}${marginBottom}`">
    <div class="qp-card-main">
        <slot />
    </div>
  </div>
</template>

<script setup>

import { computed } from "vue";

// =================================================================================== //
// ===--- PROPS

const props = defineProps({
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
})

// =================================================================================== //
// ===--- COMPUTED

const isClickable = computed(() => {
    return (props.clickable ? "qp-card-clickable" : "")
})
const isOverflow = computed(() => {
    return (props.overflow ? "qp-card-overflow" : "")
})
const bgColor = computed(() => {
    if (props.bgcolor != "base") {return `qp-card-bg-${props.bgcolor}`}
    return ""
})
const height = computed(() => {
    return (props.h ? `height:${props.h};` : "")
})
const marginBottom = computed(() => {
    return (props.mb ? `margin-bottom:${props.mb};` : "")
})

</script>

<style scoped>
    .qp-card {
        background-color: var(--qp-base);
        color: var(--qp-secondary);
        border-radius: 4px;
        box-shadow: 0 0 3px rgba(0, 0, 0, 0.04);
        overflow: hidden;
        text-align: center;
        align-content: center;
        justify-content: center;
        height: 100%;
        transition: box-shadow 0.3s, color 0.3s, opacity 0.3s;
    }
    .qp-card.qp-card-clickable:hover {
        color: var(--qp-primary);
        cursor: pointer;
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
