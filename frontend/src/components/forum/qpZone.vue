<template>
    <article v-if="props.zone" class="qp-forum-zone">
        <div class="qp-forum-zone-inner">
            <header class="qp-forum-header">
                <h2 class="qp-forum-header-title">
                    <span v-text="props.zone.name"></span>
                </h2>
                <p v-if="props.zone.description" class="qp-forum-header-description" v-text="props.zone.description"></p>
                <hr class="qp-forum-header-divider" />
                <qpForumBreadcrumbs v-if="singleton == 'zone'" :crumbs="listBreadcrumbs" />
            </header>
            <section class="qp-forum-territories">
                <qpForumTerritory v-for="(territory, n) in props.zone.territories" :key="`territory-${n}`" :world="props.world" :zone="props.zone" :territory="territory" :singleton="props.singleton" />
            </section>
        </div>
    </article>
</template>

<script setup>

import { computed } from "vue";
// import i18n from "@/plugins/i18n";
import qpForumTerritory from "@/components/forum/qpTerritory.vue";
import qpForumBreadcrumbs from "@/components/forum/qpBreadcrumbs.vue";

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
    singleton: {
        type: String,
        default: "zone"
    }
})

// =================================================================================== //
// ===--- DATA

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

// =================================================================================== //

</script>
