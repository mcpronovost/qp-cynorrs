<template>
    <article v-if="props.message" :id="`m${props.message.id}`" class="qp-forum-message">
        <div class="qp-forum-message-inner">
            <header class="qp-forum-header">
                <div v-text="props.message.author.name"></div>
            </header>
            <div class="qp-forum-message-text">
                <div class="qp-forum-message-text-inner">
                    <div v-text="props.message.text"></div>
                </div>
            </div>
        </div>
    </article>
</template>

<script setup>

// import { computed } from "vue";
// import i18n from "@/plugins/i18n";

// =================================================================================== //

// const { t } = i18n.global

// =================================================================================== //
// ===--- PROPS

const props = defineProps({
    world: {
        type: Object,
        default: () => {}
    },
    zone: {
        type: Object,
        default: () => {}
    },
    territory: {
        type: Object,
        default: () => {}
    },
    sector: {
        type: Object,
        default: () => {}
    },
    chapter: {
        type: Object,
        default: () => {}
    },
    message: {
        type: Object,
        default: () => {}
    },
    singleton: {
        type: String,
        default: "chapter"
    }
})

// =================================================================================== //

</script>
