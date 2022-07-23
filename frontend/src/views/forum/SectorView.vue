<template>
    <div class="qp-vue qp-forum qp-singleton-sector">

        <div v-if="!isLoading && !hasError && sector">
            <div class="qp-container">
                <section class="qp-forum-territories">
                    <article :id="`s${sector.id}`" class="qp-forum-sector">
                        <div class="qp-forum-sector-inner">
                            <qpForumHeader :title="sector.name" :description="sector.description" :crumbs="listBreadcrumbs" />
                            <template v-if="!showNewChapter">
                                <section>
                                    <el-row >
                                        <el-col :span="24" :md="12" :lg="17">
                                            <qpCard>
                                                (en construction)
                                            </qpCard>
                                        </el-col>
                                        <el-col :span="24" :md="12" :lg="7">
                                            <qpCard clickable bgcolor="primary" @click="openNewChapter()">
                                                <span v-text="$t('NewChapter')"></span>
                                            </qpCard>
                                        </el-col>
                                        <el-col :span="24" :lg="17" style="padding:0">
                                            <section class="qp-forum-chapters">
                                                <qpForumChapter v-for="(c, n) in sector.chapters" :key="`chapter-${n}`" :world="props.world" :territory="sector.territory" :sector="sector" :chapter="c" />
                                                <el-pagination v-if="sector.chapters.length" background hide-on-single-page layout="prev, pager, next" :total="sector.count_chapters" :page-size="sector.perpage_chapters" :current-page="paginateCurrentPage" @update:current-page="updateCurrentPage" />
                                            </section>
                                        </el-col>
                                        <el-col :span="24" :lg="7">
                                            <qpCardQuestsList />
                                        </el-col>
                                    </el-row>
                                </section>
                            </template>
                            <template v-else>
                                <qpForumWriting type="chapter" :territory="props.territory" :sector="sector" @close="closeNewChapter()" />
                            </template>
                        </div>
                    </article>
                </section>
            </div>
        </div>

        <qpForumLoadError v-else :isloading="isLoading" :hasError="hasError" />

    </div>
</template>

<script setup>

import { computed, onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
import { API } from "@/main.js";
import { slugify } from "@/plugins/filters/slugify";
import i18n from "@/plugins/i18n";

import qpCard from "@/components/basic/qpCard.vue";
import qpCardQuestsList from "@/components/widget/qpCardQuestsList.vue";
import qpForumHeader from "@/components/forum/core/qpHeader.vue";
import qpForumLoadError from "@/components/forum/core/qpLoadError.vue";
import qpForumWriting from "@/components/forum/qpWriting.vue";
import qpForumChapter from "@/components/forum/qpChapterList.vue";

const { t } = i18n.global

const route = useRoute()
const router = useRouter()
const store = useStore()
const rat = computed(() => store.getters.rat)

const props = defineProps({
    world: {
        type: Object,
        default: () => {}
    }
})

const isLoading = ref(true)
const hasError = ref(null)

const listBreadcrumbs = computed(() => {
    let result = [
        {
            name: sector.value.forum.name,
            go: `/w/${route.params.slug}/forum`
        }
    ]
    if (sector.value?.zone) {
        result.push({
            name: sector.value.zone.name,
            go: `/w/${route.params.slug}/forum/z${route.params.zone_pk}-${route.params.zone_slug}`
        })
    }
    if (sector.value?.territory) {
        result.push({
            name: sector.value.territory.name,
            go: `/w/${route.params.slug}/forum/z${route.params.zone_pk}-${route.params.zone_slug}/t${route.params.territory_pk}-${route.params.territory_slug}`
        })
    }
    return result
})

onMounted(() => {
    initForumSector()
})

const sector = ref(null)

const initForumSector = async () => {
    isLoading.value = true
    hasError.value = null
    // ===---
    try {
        let response = await fetch(`${API}/worlds/sectors/${route.params.sector_pk}/`, {
            method: "GET",
            headers: {"Authorization": rat.value}
        })
        let r = await response.json()
        if (response.status === 200) {
            sector.value = r
        } else {
            throw response
        }
    } catch (e) {
        if (e.status === 403) {
            hasError.value = t("YouDoesntHaveAccessToThisSector")
        } else if (e.status === 404) {
            hasError.value = t("ThisSectorDoesntExistAnymore")
        } else {
            hasError.value = t("AnErrorOccurred")
        }
    }
    // ===---
    isLoading.value = false
}

const paginateCurrentPage = computed(() => {
    let result = 1
    if ("page" in route.query && Number(route.query.page) > 0) {
        result = Number(route.query.page)
    }
    return result
})

const updateCurrentPage = ($event) => {
    router.push({name: "WorldForumSector", params: {
        slug: route.params.slug,
        zone_pk: route.params.zone_pk,
        zone_slug: route.params.zone_slug,
        territory_pk: route.params.territory_pk,
        territory_slug: route.params.territory_slug,
        sector_pk: sector.value.id,
        sector_slug: slugify(sector.value.name)
    },
    query: {
        page: $event
    }})
}

const showNewChapter = ref(false)

const openNewChapter = () => {
    showNewChapter.value = true
}

const closeNewChapter = () => {
    showNewChapter.value = false
}

</script>
