<template>
    <article v-if="props.sector" :id="`s${props.sector.id}`" class="qp-forum-sector" :style="`flex-basis:${props.sector.flexbasis};`">
        <div class="qp-forum-sector-inner">
            <header class="qp-forum-header">
                <el-popover :disabled="!props.sector.description || !['territory'].includes(props.singleton)" :show-after="1000">
                    <template #reference>
                        <h2 class="qp-forum-header-title" @click="goToSector(props.sector)">
                            <span v-text="props.sector.name"></span>
                        </h2>
                    </template>
                    <template #default>
                        <p class="qp-forum-header-description" v-text="props.sector.description"></p>
                    </template>
                </el-popover>
                <p v-if="['sector'].includes(props.singleton) && props.sector.description" class="qp-forum-header-description" v-text="props.sector.description"></p>
                <div v-if="['territory'].includes(props.singleton)" class="qp-forum-header-lastmessage">
                    <div :class="`qp-forum-header-lastmessage-avatar ${props.sector.last_message ? '' : 'qp-empty'}`">
                        <el-avatar v-if="props.sector.last_message" :src="props.sector.last_message?.author?.avatar">
                            <span v-text="props.sector.last_message?.author?.initials"></span>
                        </el-avatar>
                        <div v-if="props.sector.last_message" class="qp-forum-header-lastmessage-gotolast" @click="goToRoute(props.sector.last_message.routes.message)">
                            <el-icon class="mdi mdi-arrow-bottom-right-thin-circle-outline" />
                        </div>
                    </div>
                    <div class="qp-forum-header-lastmessage-infos">
                        <div class="qp-forum-header-lastmessage-infos-link" @click="goToRoute(props.sector.last_message.routes.chapter)">
                            <span v-if="props.sector.last_message" class="title" v-text="props.sector.last_message.title"></span>
                            <span v-if="props.sector.last_message" class="date" v-text="props.sector.last_message.date"></span>
                            <span v-else class="date" v-text="$t('Never')"></span>
                        </div>
                    </div>
                </div>
                <div v-if="['sector'].includes(props.singleton)">
                    <qpActionTravel :territory="props.territory" :sector="props.sector" />
                </div>
                <hr v-if="['sector'].includes(props.singleton)" class="qp-forum-header-divider" />
                <qpForumBreadcrumbs v-if="['sector'].includes(props.singleton)" :crumbs="listBreadcrumbs" />
            </header>
            <section v-if="['sector'].includes(props.singleton)" class="qp-forum-chapters">
                <qpForumChapter v-for="(chapter, n) in props.sector.chapters" :key="`chapter-${n}`" :world="props.world" :zone="props.zone" :territory="props.territory" :sector="sector" :chapter="chapter" :singleton="props.singleton" />
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

import qpActionTravel from "@/components/action/qpTravel.vue";
import qpForumBreadcrumbs from "@/components/forum/qpBreadcrumbs.vue";
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

const paginateCurrentPage = computed(() => {
    let result = 1
    if (props.singleton.includes("sector") && "page" in route.query && Number(route.query.page) > 0) {
        result = Number(route.query.page)
    }
    return result
})

// =================================================================================== //
// ===--- METHODS

const goToSector = (sector) => {
    router.push({name: "WorldForumSector", params: {
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

const updateCurrentPage = ($event) => {
    router.push({name: "WorldForumSector", params: {
        world_pk: props.world.id,
        slug: props.world.slug,
        zone_pk: props.zone.id,
        zone_slug: slugify(props.zone.name),
        territory_pk: props.territory.id,
        territory_slug: slugify(props.territory.name),
        sector_pk: props.sector.id,
        sector_slug: slugify(props.sector.name)
    },
    query: {
        page: $event
    }})
}

// =================================================================================== //

</script>
