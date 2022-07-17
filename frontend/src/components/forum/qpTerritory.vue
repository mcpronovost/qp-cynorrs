<template>
    <article v-if="props.territory" :id="`t${props.territory.id}`" class="qp-forum-territory" :style="`flex-basis:${props.territory.flexbasis};`">
        <div class="qp-forum-territory-inner">
            <header class="qp-forum-header">
                <h2 class="qp-forum-header-title" @click="goToTerritory(props.territory)">
                    <span v-text="props.territory.name"></span>
                </h2>
                <p v-if="props.territory.description" class="qp-forum-header-description" v-text="props.territory.description"></p>
                <hr v-if="props.singleton.includes('territory')" class="qp-forum-header-divider" />
                <qpForumBreadcrumbs v-if="props.singleton.includes('territory')" :crumbs="listBreadcrumbs" />
            </header>
            <section v-if="props.singleton.includes('territory')" class="qp-forum-sectors">
                <qpForumSector v-for="(sector, n) in props.territory.sectors" :key="`sector-${n}`" :world="props.world" :zone="props.zone" :territory="props.territory" :sector="sector" :singleton="props.singleton" />
            </section>
            <section v-if="props.singleton.includes('territory')" class="qp-forum-chapters">
                <qpForumChapter v-for="(chapter, n) in props.territory.chapters" :key="`chapter-${n}`" :world="props.world" :zone="props.zone" :territory="props.territory" :chapter="chapter" :singleton="props.singleton" />
                <el-pagination
                    background
                    hide-on-single-page
                    layout="prev, pager, next"
                    :total="props.territory.count_chapters"
                    :page-size="props.territory.perpage_chapters"
                    :current-page="paginateCurrentPage"
                    @update:current-page="updateCurrentPage"
                />
            </section>
        </div>
    </article>
</template>

<script setup>

import { computed } from "vue";
// import i18n from "@/plugins/i18n";
import { useRoute, useRouter } from "vue-router";
import { slugify } from "@/plugins/filters/slugify";
import qpForumBreadcrumbs from "@/components/forum/qpBreadcrumbs.vue";
import qpForumSector from "@/components/forum/qpSector.vue";
import qpForumChapter from "@/components/forum/qpChapter.vue";

// =================================================================================== //

// const { t } = i18n.global
const route = useRoute()
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
    singleton: {
        type: String,
        default: "territory"
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
        }
    ]
    return result
})

const paginateCurrentPage = computed(() => {
    let result = 1
    if (props.singleton.includes("territory") && "page" in route.query && Number(route.query.page) > 0) {
        result = Number(route.query.page)
    }
    return result
})

// =================================================================================== //
// ===--- METHODS

const goToTerritory = (territory) => {
    router.push({name: "WorldTerritory", params: {
        world_pk: props.world.id,
        slug: props.world.slug,
        zone_pk: props.zone.id,
        zone_slug: slugify(props.zone.name),
        territory_pk: territory.id,
        territory_slug: slugify(territory.name)
    }})
}

const updateCurrentPage = ($event) => {
    router.push({name: "WorldTerritory", params: {
        world_pk: props.world.id,
        slug: props.world.slug,
        zone_pk: props.zone.id,
        zone_slug: slugify(props.zone.name),
        territory_pk: props.territory.id,
        territory_slug: slugify(props.territory.name)
    },
    query: {
        page: $event
    }})
}

// =================================================================================== //

</script>
