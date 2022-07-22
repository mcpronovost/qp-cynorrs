<template>
    <article v-if="props.zone" :id="`z${props.zone.id}`" class="qp-forum-zone">
        <div class="qp-forum-zone-inner">
            <qpForumHeader :title="props.zone.name" :description="props.zone.description" :crumbs="listBreadcrumbs" />
            <section class="qp-forum-territories">
                <qpForumTerritory v-for="(t, n) in props.zone.territories" :key="`territory-${n}`" :territory="t" />
            </section>
        </div>
    </article>
</template>

<script setup>

import { computed } from "vue";
import { useRoute } from "vue-router";

import qpForumHeader from "@/components/forum/core/qpHeader.vue";
import qpForumTerritory from "@/components/forum/qpTerritoryList.vue";

const route = useRoute()

const props = defineProps({
    world: {
        type: Object,
        default: () => {}
    },
    zone: {
        type: Object,
        default: () => {}
    }
})

const listBreadcrumbs = computed(() => {
    if (route.name == "WorldForum") {
        return []
    }
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
