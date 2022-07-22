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
                        <span v-if="props.chapter.last_message" v-text="$filters.date_to_str(props.chapter.last_message.created_at)"></span>
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
import { slugify } from "@/plugins/filters/slugify";

const router = useRouter()

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
    }
})

const goToChapter = (chapter) => {
    router.push({name: "WorldForumChapter", params: {
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

// =================================================================================== //

</script>
