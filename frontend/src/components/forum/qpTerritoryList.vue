<template>
    <article v-if="props.territory" :id="`t${props.territory.id}`" class="qp-forum-territory" :style="`flex-basis:${props.territory.flexbasis};`">
        <div class="qp-forum-territory-inner">
            <header class="qp-forum-header">
                <el-popover :show-after="1000" popper-class="qp-forum-header-popper">
                    <template #reference>
                        <h2 class="qp-forum-header-title" @click="goToTerritory()" :style="props.territory.colour ? `color:${props.territory.colour};` : ''">
                            <span v-text="props.territory.name"></span>
                        </h2>
                    </template>
                    <template #default>
                        <el-row>
                            <el-col v-if="props.territory.description" :span="24">
                                <p class="qp-forum-popheader-description" v-text="props.territory.description"></p>
                            </el-col>
                            <el-col v-if="props.territory.count_sectors" :span="8" align="center">
                                <span v-text="numtostr(props.territory.count_sectors)"></span>
                                <div>
                                    <span v-text="$t('Sector', props.territory.count_sectors)"></span>
                                </div>
                            </el-col>
                            <el-col :span="props.territory.count_sectors ? 8 : 12" align="center">
                                <span v-text="numtostr(props.territory.count_chapters)"></span>
                                <div>
                                    <span v-text="$t('Chapter', props.territory.count_chapters)"></span>
                                </div>
                            </el-col>
                            <el-col :span="props.territory.count_sectors ? 8 : 12" align="center">
                                <span v-text="numtostr(props.territory.count_messages)"></span>
                                <div>
                                    <span v-text="$t('Message', props.territory.count_messages)"></span>
                                </div>
                            </el-col>
                        </el-row>
                    </template>
                </el-popover>
                <div class="qp-forum-header-lastmessage">
                    <div :class="`qp-forum-header-lastmessage-avatar ${props.territory.last_chapter?.last_message ? '' : 'qp-empty'}`">
                        <el-avatar v-if="props.territory.last_chapter?.last_message" :src="props.territory.last_chapter.last_message.author?.avatar">
                            <span v-text="props.territory.last_chapter.last_message.author?.initials"></span>
                        </el-avatar>
                        <div v-if="props.territory.last_chapter?.last_message" class="qp-forum-header-lastmessage-gotolast" @click="goToRoute(props.territory.last_chapter.last_message.route)">
                            <el-icon class="mdi mdi-arrow-bottom-right-thin-circle-outline" />
                        </div>
                        <div v-if="props.territory.last_chapter && props.territory.is_unread" class="qp-forum-header-lastmessage-unread">
                            <el-icon class="mdi mdi-bell" />
                        </div>
                    </div>
                    <div v-if="props.territory.last_chapter?.last_message" class="qp-forum-header-lastmessage-infos">
                        <div class="qp-forum-header-lastmessage-infos-link" @click="goToRoute(props.territory.last_chapter.route)">
                            <span class="title" v-text="props.territory.last_chapter.last_message.chapter.title"></span>
                            <span class="date" v-text="datetostr(props.territory.last_chapter.last_message.created_at)"></span>
                        </div>
                    </div>
                </div>
            </header>
        </div>
    </article>
</template>

<script setup>

import { useRoute, useRouter } from "vue-router";
import { datetostr } from "@/plugins/filters/datetostr";
import { numtostr } from "@/plugins/filters/numtostr";
import { slugify } from "@/plugins/filters/slugify";

const route = useRoute()
const router = useRouter()

const props = defineProps({
    territory: {
        type: Object,
        default: () => {}
    }
})

const goToRoute = (last_route) => {
    if (last_route) {
        router.push(last_route)
    }
}

const goToTerritory = () => {
    router.push({name: "WorldForumTerritory", params: {
        slug: route.params.slug,
        zone_pk: props.territory.zone.id,
        zone_slug: slugify(props.territory.zone.name),
        territory_pk: props.territory.id,
        territory_slug: slugify(props.territory.name)
    }})
}

</script>
