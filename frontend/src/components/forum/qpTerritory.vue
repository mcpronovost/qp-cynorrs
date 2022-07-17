<template>
    <article v-if="props.territory" :id="`t${props.territory.id}`" class="qp-forum-territory" :style="`flex-basis:${props.territory.flexbasis};`">
        <div class="qp-forum-territory-inner">
            <header class="qp-forum-header">
                <el-popover :disabled="!props.territory.description || !['index', 'zone'].includes(props.singleton)" :show-after="1000">
                    <template #reference>
                        <h2 class="qp-forum-header-title" @click="goToTerritory(props.territory)" :style="props.territory.colour ? `color:${props.territory.colour};` : ''">
                            <span v-text="props.territory.name"></span>
                        </h2>
                    </template>
                    <template #default>
                        <p class="qp-forum-header-description" v-text="props.territory.description"></p>
                    </template>
                </el-popover>
                <p v-if="['territory'].includes(props.singleton) && props.territory.description" class="qp-forum-header-description" v-text="props.territory.description"></p>
                <div v-if="['index', 'zone'].includes(props.singleton)" class="qp-forum-header-lastmessage">
                    <div class="qp-forum-header-lastmessage-avatar">
                        <el-avatar v-if="props.territory.last_message" :src="props.territory.last_message?.author?.avatar">
                            <span v-text="props.territory.last_message?.author?.initials"></span>
                        </el-avatar>
                        <div v-if="props.territory.last_message" class="qp-forum-header-lastmessage-gotolast" @click="goToRoute(props.territory.last_message.routes.message)">
                            <el-icon class="mdi mdi-arrow-bottom-right-thin-circle-outline" />
                        </div>
                    </div>
                    <div v-if="props.territory.last_message" class="qp-forum-header-lastmessage-infos">
                        <div class="qp-forum-header-lastmessage-infos-link" @click="goToRoute(props.territory.last_message.routes.chapter)">
                            <span class="title" v-text="props.territory.last_message.title"></span>
                            <span class="date" v-text="props.territory.last_message.date"></span>
                        </div>
                    </div>
                </div>
                <div v-if="['territory'].includes(props.singleton)">
                    <qpActionTravel :territory="props.territory" />
                </div>
                <hr v-if="['territory'].includes(props.singleton)" class="qp-forum-header-divider" />
                <qpForumBreadcrumbs v-if="['territory'].includes(props.singleton)" :crumbs="listBreadcrumbs" />
            </header>
            <section v-if="['territory'].includes(props.singleton)" class="qp-forum-sectors">
                <qpForumSector v-for="(sector, n) in props.territory.sectors" :key="`sector-${n}`" :world="props.world" :zone="props.zone" :territory="props.territory" :sector="sector" :singleton="props.singleton" />
            </section>
            <section v-if="['territory'].includes(props.singleton)" class="qp-forum-chapters">
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

import qpActionTravel from "@/components/action/qpTravel.vue";
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

const goToRoute = (last_route) => {
    if (last_route) {
        router.push(last_route)
    }
}

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

<style scoped>

.qp-forum-header-lastmessage {
    display: flex;
    flex: 1 1 auto;
    flex-direction: column;
    padding: 0 12px 12px;
}
.qp-forum-header-lastmessage-avatar {
    border-radius: 100%;
    overflow: hidden;
    flex: 0 0 auto;
    align-self: flex-end;
    width: 110px;
    height: 110px;
    position: relative;
    margin: 0 auto;
}
.qp-forum-header-lastmessage-avatar .el-avatar {
    width: 100%;
    height: 100%;
}
.qp-forum-header-lastmessage-avatar:hover {
    cursor: pointer;
}
.qp-forum-header-lastmessage-gotolast {
    background-color: var(--qp-base);
    border-radius: 100%;
    font-size: 64px;
    line-height: 106px;
    position: absolute;
    top: 2px;
    left: 2px;
    right: 2px;
    bottom: 2px;
    opacity: 0;
    transition: opacity 0.4s;
}
.qp-forum-header-lastmessage-avatar:hover .qp-forum-header-lastmessage-gotolast {
    opacity: 0.8;
}
.qp-forum-header-lastmessage-infos {
    font-family: "Roboto Condensed", sans-serif;
    font-size: 12px;
    font-weight: 400;
    line-height: 120%;
    letter-spacing: 1px;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    padding: 24px 12px 12px;
}
.qp-forum-header-lastmessage-infos-link {
    transition: opacity 0.3s;
}
.qp-forum-header-lastmessage-infos-link:hover {
    opacity: 0.7;
    cursor: pointer;
}
.qp-forum-header-lastmessage-infos-link span.title {
    color: var(--qp-primary);
    display: block;
    padding: 0 6px;
}
.qp-forum-header-lastmessage-infos-link span.date {
    color: var(--qp-tertiary);
    display: block;
    padding: 4px 6px 0;
}

</style>
