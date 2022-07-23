<template>
    <article v-if="props.sector" :id="`t${props.sector.id}`" class="qp-forum-sector" :style="`flex-basis:${props.sector.flexbasis};`">
        <div class="qp-forum-sector-inner">
            <header class="qp-forum-header">
                <el-popover :show-after="1000" popper-class="qp-forum-header-popper">
                    <template #reference>
                        <h2 class="qp-forum-header-title" @click="goToSector()" :style="props.sector.colour ? `color:${props.sector.colour};` : ''">
                            <span v-text="props.sector.name"></span>
                        </h2>
                    </template>
                    <template #default>
                        <el-row>
                            <el-col v-if="props.sector.description" :span="24">
                                <p class="qp-forum-popheader-description" v-text="props.sector.description"></p>
                            </el-col>
                            <el-col :span="12" align="center">
                                <span v-text="numtostr(props.sector.count_chapters)"></span>
                                <div>
                                    <span v-text="$t('Chapter', props.sector.count_chapters)"></span>
                                </div>
                            </el-col>
                            <el-col :span="12" align="center">
                                <span v-text="numtostr(props.sector.count_messages)"></span>
                                <div>
                                    <span v-text="$t('Message', props.sector.count_messages)"></span>
                                </div>
                            </el-col>
                        </el-row>
                    </template>
                </el-popover>
                <div v-if="false" class="qp-forum-header-lastmessage">
                    <div :class="`qp-forum-header-lastmessage-avatar ${props.territory.last_chapter?.last_message ? '' : 'qp-empty'}`">
                        <el-avatar v-if="props.territory.last_chapter?.last_message" :src="props.territory.last_chapter.last_message.author?.avatar">
                            <span v-text="props.territory.last_chapter.last_message.author?.initials"></span>
                        </el-avatar>
                        <div v-if="props.territory.last_chapter?.last_message" class="qp-forum-header-lastmessage-gotolast" @click="goToRoute(props.territory.last_chapter.last_message.route)">
                            <el-icon class="mdi mdi-arrow-bottom-right-thin-circle-outline" />
                        </div>
                    </div>
                    <div v-if="props.territory.last_chapter?.last_message" class="qp-forum-header-lastmessage-infos">
                        <div class="qp-forum-header-lastmessage-infos-link" @click="goToRoute(props.territory.last_chapter.route)">
                            <span class="title" v-text="props.territory.last_chapter.last_message.chapter.title"></span>
                            <span class="date" v-text="datetostr(props.territory.last_chapter.last_message.chapter.created_at)"></span>
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
    world: {
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
    }
})

const goToRoute = (last_route) => {
    if (last_route) {
        router.push(last_route)
    }
}

const goToSector = () => {
    router.push({name: "WorldForumSector", params: {
        slug: route.params.slug,
        zone_pk: route.params.zone_pk,
        zone_slug: route.params.zone_slug,
        territory_pk: route.params.territory_pk,
        territory_slug: route.params.territory_slug,
        sector_pk: props.sector.id,
        sector_slug: slugify(props.sector.name)
    }})
}

</script>
