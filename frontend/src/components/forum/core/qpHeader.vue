<template>
    <header class="qp-forum-header">
        <h2 class="qp-forum-header-title">
            <span v-text="props.title"></span>
        </h2>
        <p v-if="props.description" class="qp-forum-header-description" v-text="props.description"></p>
        <hr class="qp-forum-header-divider" />
        <qpForumBreadcrumbs v-if="props.crumbs?.length" :crumbs="props.crumbs" />
    </header>
</template>

<script setup>

import qpForumBreadcrumbs from "@/components/forum/core/qpBreadcrumbs.vue";

const props = defineProps({
    title: {
        type: String,
        default: ""
    },
    description: {
        type: String,
        default: null
    },
    crumbs: {
        type: Object,
        default: () => {}
    }
})

</script>
