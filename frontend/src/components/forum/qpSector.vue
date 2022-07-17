<template>
    <article v-if="props.sector" :id="`s${props.sector.id}`" class="qp-forum-sector" :style="`flex-basis:${props.sector.flexbasis};`">
        <div class="qp-forum-sector-inner">
            <header class="qp-forum-header">
                <h2 class="qp-forum-header-title" @click="goToSector(props.sector)">
                    <span v-text="props.sector.name"></span>
                </h2>
                <p v-if="singleton == 'sector' && props.sector.description" class="qp-forum-header-description" v-text="props.sector.description"></p>
                <hr v-if="singleton == 'sector'" class="qp-forum-header-divider" />
                <qpForumBreadcrumbs v-if="singleton == 'sector'" :crumbs="listBreadcrumbs" />
            </header>
            <section v-if="props.singleton == 'sector'" class="qp-forum-chapters">
                <qpForumChapter v-for="(chapter, n) in props.sector.chapters" :key="`chapter-${n}`" :world="props.world" :zone="props.zone" :territory="props.territory" :sector="sector" :chapter="chapter" :singleton="props.singleton" />
            </section>
        </div>
    </article>
</template>

<script setup>

import { computed } from "vue";
// import i18n from "@/plugins/i18n";
import { useRouter } from "vue-router";
import { slugify } from "@/plugins/filters/slugify";
import qpForumBreadcrumbs from "@/components/forum/qpBreadcrumbs.vue";
import qpForumChapter from "@/components/forum/qpChapter.vue";

// =================================================================================== //

// const { t } = i18n.global
const router = useRouter()

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
    singleton: {
        type: String,
        default: "sector"
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
        },
        {
            name: props.zone.name,
            view: "zone",
            data: {
                world: props.world,
                zone: props.zone
            }
        },
        {
            name: props.territory.name,
            view: "territory",
            data: {
                world: props.world,
                zone: props.zone,
                territory: props.territory
            }
        }
    ]
    return result
})

// =================================================================================== //
// ===--- METHODS

const goToSector = (sector) => {
    router.push({name: "WorldSector", params: {
        world_pk: props.world.id,
        slug: props.world.slug,
        zone_pk: props.zone.id,
        zone_slug: slugify(props.zone.name),
        territory_pk: props.territory.id,
        territory_slug: slugify(props.territory.name),
        sector_pk: sector.id,
        sector_slug: slugify(sector.name)
    }})
}

// =================================================================================== //

</script>
