<template>
    <div class="qp-vue qp-forum qp-singleton-zone">

        <div v-if="!isLoading && !hasError && chapter">
            <div class="qp-container">
                <section class="qp-forum-chapters">
                    <article v-if="chapter" :id="`c${chapter.id}`" class="qp-forum-chapter">
                        <div class="qp-forum-chapter-inner">
                            <qpForumHeader :title="chapter.title" :description="chapter.description" :crumbs="listBreadcrumbs" />
                            <section v-if="chapter.messages?.length" class="qp-forum-messages">
                                <qpForumMessage v-for="(m, n) in chapter.messages" :key="`message-${n}`" :world="props.world" :chapter="chapter" :message="m" />
                                <el-pagination background hide-on-single-page layout="prev, pager, next" :total="chapter.count_messages" :page-size="chapter.perpage_messages" :current-page="paginateCurrentPage" @update:current-page="updateCurrentPage" />
                            </section>
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
import { useRoute } from "vue-router";
import { useStore } from "vuex";
import { API } from "@/main.js";
import i18n from "@/plugins/i18n";

import qpForumHeader from "@/components/forum/core/qpHeader.vue";
import qpForumLoadError from "@/components/forum/core/qpLoadError.vue";
import qpForumMessage from "@/components/forum/qpMessage.vue";

const { t } = i18n.global

const route = useRoute()
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

onMounted(() => {
    initForumChapter()
})

const chapter = ref(null)

const initForumChapter = async () => {
    isLoading.value = true
    hasError.value = null
    // ===---
    try {
        let response = await fetch(`${API}/worlds/chapters/${route.params.chapter_pk}/`, {
            method: "GET",
            headers: {"Authorization": rat.value}
        })
        let r = await response.json()
        if (response.status === 200) {
            chapter.value = r
        } else {
            throw response
        }
    } catch (e) {
        if (e.status === 403) {
            hasError.value = t("YouDoesntHaveAccessToThisChapter")
        } else if (e.status === 404) {
            hasError.value = t("ThisChapterDoesntExistAnymore")
        } else {
            hasError.value = t("AnErrorOccurred")
        }
    }
    // ===---
    isLoading.value = false
}

const listBreadcrumbs = computed(() => {
    let result = [
        {
            name: props.world.name,
            go: `/w/${route.params.slug}/forum`
        }
    ]
    if (chapter.value) {
        result.push({
            name: chapter.value.territory.zone.name,
            go: `/w/${route.params.slug}/forum/z${route.params.zone_pk}-${route.params.zone_slug}`
        })
    }
    if (chapter.value) {
        result.push({
            name: chapter.value.territory.name,
            go: `/w/${route.params.slug}/forum/z${route.params.zone_pk}-${route.params.zone_slug}/t${route.params.territory_pk}-${route.params.territory_slug}`
        })
    }
    if (chapter.value?.sector) {
        result.push({
            name: chapter.value.sector.name,
            go: `/w/${route.params.slug}/forum/z${route.params.zone_pk}-${route.params.zone_slug}/t${route.params.territory_pk}-${route.params.territory_slug}/s${route.params.sector_pk}-${route.params.sector_slug}`
        })
    }
    return result
})

const paginateCurrentPage = computed(() => {
    let result = 1
    if ("page" in route.query && Number(route.query.page) > 0) {
        result = Number(route.query.page)
    }
    return result
})

</script>
