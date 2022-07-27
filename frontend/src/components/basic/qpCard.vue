<template>
  <div :class="`qp-card ${isClickable} ${isOverflow} ${bgColor}`" :style="`${height}${marginBottom}`">
    <div v-if="$slots.header" class="qp-card-header">
        <div class="qp-card-header-title">
            <slot name="header" />
        </div>
    </div>
    <div class="qp-card-main" :style="`${padding}`">
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
    pa: {
        type: String,
        default: "20px"
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
const padding = computed(() => {
    return (props.pa ? `padding:${props.pa};` : "")
})
const marginBottom = computed(() => {
    return (props.mb ? `margin-bottom:${props.mb};` : "")
})

</script>

<style scoped>
    .qp-card {
        background-color: var(--qp-default-bg);
        color: var(--qp-default-txt);
        border-radius: 4px;
        box-shadow: 0 0 3px rgba(0, 0, 0, 0.04);
        overflow: hidden;
        text-align: center;
        align-content: center;
        justify-content: center;
        height: 100%;
        transition: box-shadow 0.3s, color 0.3s, opacity 0.3s;
    }
    .qp-card.qp-card-clickable:hover,
    .qp-card.qp-card-clickable:focus {
        box-shadow: 0 0 3px rgba(0, 0, 0, 0.3);
        opacity: 0.6;
        cursor: pointer;
    }
    .qp-card.qp-card-clickable:active {
        opacity: 0.4;
    }
    .qp-card.qp-card-overflow {
        overflow: visible;
    }
    .qp-card.qp-card-bg-primary {
        background-color: var(--qp-default-accented-bg);
        color: var(--qp-default-accented-txt);
    }
    /* ===--- header ---=== */
    .qp-card-header {
        padding: 20px 20px 0;
    }
    .qp-card-header-title {
        font-size: 14px;
        font-weight: 600;
        line-height: 120%;
        text-align: left;
    }
    /* ===--- main ---=== */
    .qp-card-main {
        padding: 20px;
    }
</style>
