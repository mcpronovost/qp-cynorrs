<template>
    <article v-if="props.chapter" :id="`c${props.chapter.id}`" class="qp-forum-chapter">
        <div class="qp-forum-chapter-inner">
            <header class="qp-forum-header">
                <div v-if="['territory', 'sector'].includes(singleton)" class="qp-forum-header-profile">
                    <div class="qp-forum-header-profile-banner">
                        <el-image v-if="props.chapter.author?.avatar" :src="props.chapter.author.avatar" fit="cover">
                            <template #error>
                                <div class="image-slot"></div>
                            </template>
                        </el-image>
                    </div>
                    <div class="qp-forum-header-profile-avatar">
                        <el-avatar :src="props.chapter.last_message?.author?.avatar">
                            <span v-text="props.chapter.last_message?.author?.initials"></span>
                        </el-avatar>
                    </div>
                </div>
                <h2 class="qp-forum-header-title" @click="goToChapter(props.chapter)">
                    <span v-text="props.chapter.title"></span>
                </h2>
                <p class="qp-forum-header-date">
                    <span v-if="props.chapter.date" v-text="props.chapter.date"></span>
                </p>
                <ul class="qp-forum-header-infos">
                    <li class="qp-forum-header-infos-lastmessagedate">
                        <el-icon class="mdi mdi-clock-outline" />
                        <span v-if="props.chapter.last_message" v-text="props.chapter.last_message.date"></span>
                        <span v-else v-text="$t('Never')"></span>
                    </li>
                    <li class="qp-forum-header-infos-countmessages">
                        <el-icon class="mdi mdi-message-text-outline" />
                        <span v-text="props.chapter.count_messages"></span>
                    </li>
                </ul>
                <hr v-if="singleton == 'chapter'" class="qp-forum-header-divider" />
                <qpForumBreadcrumbs v-if="singleton == 'chapter'" :crumbs="listBreadcrumbs" />
            </header>
            <section v-if="props.singleton == 'chapter'" class="qp-forum-messages">
                <qpForumMessage v-for="(message, n) in props.chapter.messages" :key="`message-${n}`" :world="props.world" :zone="props.zone" :territory="props.territory" :chapter="chapter" :message="message" :singleton="props.singleton" />
            </section>
        </div>
    </article>
</template>

<script setup>

import { computed, onMounted } from "vue";
// import i18n from "@/plugins/i18n";
import { useRoute, useRouter } from "vue-router";
import { slugify } from "@/plugins/filters/slugify";
import qpForumBreadcrumbs from "@/components/forum/qpBreadcrumbs.vue";
import qpForumMessage from "@/components/forum/qpMessage.vue";

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
    chapter: {
        type: Object,
        default: () => {}
    },
    singleton: {
        type: String,
        default: "chapter"
    }
})

// =================================================================================== //
// ===--- DATA

const listBreadcrumbs = computed(() => {
    let result = []
    if (props.world) {
        result.push({
            name: props.world.name,
            view: "world",
            data: {
                world: props.world
            }
        })
    }
    if (props.zone) {
        result.push({
            name: props.zone.name,
            view: "zone",
            data: {
                world: props.world,
                zone: props.zone
            }
        })
    }
    if (props.territory) {
        result.push({
            name: props.territory.name,
            view: "territory",
            data: {
                world: props.world,
                zone: props.zone,
                territory: props.territory
            }
        })
    }
    if (props.sector) {
        result.push({
            name: props.sector.name,
            view: "sector",
            data: {
                world: props.world,
                zone: props.zone,
                territory: props.territory,
                sector: props.sector
            }
        })
    }
    return result
})

// =================================================================================== //
// ===--- METHODS

const goToChapter = (chapter) => {
    router.push({name: "WorldChapter", params: {
        world_pk: props.world.id,
        slug: props.world.slug,
        zone_pk: props.zone.id,
        zone_slug: slugify(props.zone.name),
        territory_pk: props.territory.id,
        territory_slug: slugify(props.territory.name),
        chapter_pk: chapter.id,
        chapter_slug: slugify(chapter.title)
    }})
}

onMounted(() => {
    if (route.hash && route.hash.startsWith("#c")) {
        const el = document.getElementById(route.hash.replace("#", ""))
        if (el) {
            el.scrollIntoView({behavior: "smooth"})
        }
    }
})

// =================================================================================== //

</script>
