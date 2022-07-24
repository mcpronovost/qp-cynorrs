<template>
    <div class="qp-vue qp-forum qp-singleton-territory">

        <div v-if="!isLoading && !hasError && territory">
            <div class="qp-container">
                <section class="qp-forum-territories">
                    <article :id="`t${territory.id}`" class="qp-forum-territory">
                        <div class="qp-forum-territory-inner">
                            <qpForumHeader :title="territory.name" :description="territory.description" :crumbs="listBreadcrumbs" />
                            <template v-if="!showNewChapter">
                                <section class="qp-forum-sectors">
                                    <qpForumSector v-for="(s, n) in territory.sectors" :key="`sector-${n}`" :world="props.world" :territory="territory" :sector="s" />
                                    <hr v-if="territory.sectors?.length" />
                                </section>
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
                                                <qpForumChapter v-for="(c, n) in territory.chapters" :key="`chapter-${n}`" :world="props.world" :territory="territory" :chapter="c" />
                                                <el-pagination v-if="territory.chapters.length" background hide-on-single-page layout="prev, pager, next" :total="territory.count_chapters" :page-size="territory.perpage_chapters" :current-page="paginateCurrentPage" @update:current-page="updateCurrentPage" />
                                            </section>
                                        </el-col>
                                        <el-col :span="24" :lg="7">
                                            <qpCardQuestsList />
                                        </el-col>
                                    </el-row>
                                </section>
                            </template>
                            <template v-else>
                                <qpForumWritingChapter :world="world" :territory="territory" @close="closeNewChapter()" />
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
import qpForumWritingChapter from "@/components/forum/qpWritingChapter.vue";
import qpForumSector from "@/components/forum/qpSectorList.vue";
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
            name: territory.value.forum.name,
            go: `/w/${route.params.slug}/forum`
        }
    ]
    if (territory.value) {
        result.push({
            name: territory.value.zone.name,
            go: `/w/${route.params.slug}/forum/z${route.params.zone_pk}-${route.params.zone_slug}`
        })
    }
    return result
})

onMounted(() => {
    initForumTerritory()
})

const territory = ref(null)

const initForumTerritory = async () => {
    isLoading.value = true
    hasError.value = null
    // ===---
    try {
        let response = await fetch(`${API}/worlds/territories/${route.params.territory_pk}/`, {
            method: "GET",
            headers: {"Authorization": rat.value}
        })
        let r = await response.json()
        if (response.status === 200) {
            territory.value = r
        } else {
            throw response
        }
    } catch (e) {
        if (e.status === 403) {
            hasError.value = t("YouDoesntHaveAccessToThisTerritory")
        } else if (e.status === 404) {
            hasError.value = t("ThisTerritoryDoesntExistAnymore")
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
    router.push({name: "WorldForumTerritory", params: {
        slug: route.params.slug,
        zone_pk: route.params.zone_pk,
        zone_slug: route.params.zone_slug,
        territory_pk: territory.value.id,
        territory_slug: slugify(territory.value.name)
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
