<template>
    <article v-if="props.zone" :id="`z${props.zone.id}`" class="qp-forum-zone">
        <div class="qp-forum-zone-inner">
            <qpForumHeader :title="props.zone.name" :description="props.zone.description" :crumbs="listBreadcrumbs" />
        </div>
    </article>
</template>

<script setup>

import { computed } from "vue";

import qpForumHeader from "@/components/forum/qpHeader.vue";

const props = defineProps({
    world: {
        type: Object,
        default: () => {}
    },
    forum: {
        type: Object,
        default: () => {}
    },
    zone: {
        type: Object,
        default: () => {}
    },
    singleton: {
        type: String,
        default: "zone"
    }
})

const listBreadcrumbs = computed(() => {
    let result = [
        {
            name: props.world.name,
            view: "world",
            data: {
                world: props.world
            }
        }
    ]
    return result
})

</script>
