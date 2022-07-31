<template>
    <article v-if="props.chapter" :id="`c${props.chapter.id}`" class="qp-forum-chapter">
        <div class="qp-forum-chapter-inner">
            <header class="qp-forum-header">
                <div class="qp-forum-header-profile">
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
                        <div v-if="props.chapter.last_message && props.chapter.is_unread" class="qp-forum-header-profile-unread">
                            <el-icon class="mdi mdi-bell" />
                        </div>
                    </div>
                </div>
                <h2 class="qp-forum-header-title" @click="goToChapter()">
                    <span v-text="props.chapter.title"></span>
                </h2>
                <p class="qp-forum-header-date">
                    <span v-if="props.chapter.date" v-text="props.chapter.date"></span>
                </p>
                <ul class="qp-forum-header-infos">
                    <li class="qp-forum-header-infos-lastmessagedate">
                        <el-icon class="mdi mdi-clock-outline" />
                        <span v-if="props.chapter.last_message" v-text="datetostr(props.chapter.last_message.created_at)"></span>
                        <span v-else v-text="$t('Never')"></span>
                    </li>
                    <li class="qp-forum-header-infos-countmessages">
                        <el-icon class="mdi mdi-message-text-outline" />
                        <span v-text="props.chapter.count_messages"></span>
                    </li>
                </ul>
            </header>
        </div>
    </article>
</template>

<script setup>

import { useRouter } from "vue-router";
import { datetostr } from "@/plugins/filters/datetostr";
import { slugify } from "@/plugins/filters/slugify";

const router = useRouter()

const props = defineProps({
    world: {
        type: Object,
        default: () => {}
    },
    territory: {
        type: Object,
        default: () => {}
    },
    chapter: {
        type: Object,
        default: () => {}
    }
})

const goToChapter = () => {
    router.push({name: "WorldForumTerritoryChapter", params: {
        slug: props.world.slug,
        zone_pk: props.territory.zone.id,
        zone_slug: slugify(props.territory.zone.name),
        territory_pk: props.territory.id,
        territory_slug: slugify(props.territory.name),
        chapter_pk: props.chapter.id,
        chapter_slug: slugify(props.chapter.title)
    }})
}

// =================================================================================== //

</script>
