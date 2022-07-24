<template>
    <div class="qp-vue qp-forum qp-singleton-zone">

        <div v-if="!isLoading && !hasError && chapter">
            <div class="qp-container">
                <section class="qp-forum-chapters">
                    <article v-if="chapter" :id="`c${chapter.id}`" class="qp-forum-chapter">
                        <div class="qp-forum-chapter-inner">
                            <qpForumHeader show-btn-reply :title="chapter.title" :description="chapter.description" :crumbs="listBreadcrumbs" @open-new-reply="openNewReply()" />
                            <section v-if="messages" class="qp-forum-messages">
                                <qpForumMessage v-for="(m, n) in messages.results" :key="`message-${n}`" :world="props.world" :chapter="chapter" :message="m" />
                            </section>
                            <qpForumFooter show-btn-reply :crumbs="listBreadcrumbs" @open-new-reply="openNewReply()" />
                            <el-pagination v-if="messages?.results.length" background hide-on-single-page layout="prev, pager, next" :total="messages.count" :page-size="messages.size" :current-page="paginateCurrentPage" @update:current-page="updateCurrentPage" />
                        </div>
                    </article>
                </section>
                <section v-if="showWritingReply" id="reply" class="qp-forum-writing">
                    <qpForumWritingReply :world="props.world" :chapter="chapter" @close="closeNewReply()" />
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
import i18n from "@/plugins/i18n";

import qpForumHeader from "@/components/forum/core/qpHeader.vue";
import qpForumFooter from "@/components/forum/core/qpFooter.vue";
import qpForumLoadError from "@/components/forum/core/qpLoadError.vue";
import qpForumMessage from "@/components/forum/qpMessage.vue";
import qpForumWritingReply from "@/components/forum/qpWritingReply.vue";

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
            name: chapter.value.forum.name,
            go: `/w/${route.params.slug}/forum`
        }
    ]
    if (chapter.value) {
        result.push({
            name: chapter.value.zone.name,
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

onMounted(() => {
    initForumChapter()
})

const chapter = ref(null)
const messages = ref(null)

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
            initForumChapterMessages()
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

const initForumChapterMessages = async () => {
    isLoading.value = true
    hasError.value = null
    // ===---
    try {
        let response = await fetch(`${API}/worlds/chapters/${route.params.chapter_pk}/messages/?page=${paginateCurrentPage.value}`, {
            method: "GET",
            headers: {"Authorization": rat.value}
        })
        let r = await response.json()
        if (response.status === 200) {
            messages.value = r
            scrollToHash()
        } else {
            throw response
        }
    } catch (e) {
        if (e.status === 403) {
            hasError.value = t("YouDoesntHaveAccessToThisChapter")
        } else if (e.status === 404) {
            hasError.value = t("ThisPageDoesntExistAnymore")
        } else {
            hasError.value = t("AnErrorOccurred")
        }
    }
    // ===---
    isLoading.value = false
}

const scrollToHash = () => {
    setTimeout(() => {
        if (route.hash && (route.hash.startsWith("#c") || route.hash.startsWith("#m"))) {
            const el = document.getElementById(route.hash.replace("#", ""))
            if (el) {
                el.scrollIntoView({behavior: "smooth"})
            }
        }
    }, 200)
}

const paginateCurrentPage = computed(() => {
    let result = 1
    if ("page" in route.query && Number(route.query.page) > 0) {
        result = Number(route.query.page)
    }
    return result
})

const updateCurrentPage = ($event) => {
    let routename = "WorldForumTerritoryChapter"
    let routeobj = {
        name: routename,
        params: {
            slug: route.params.slug,
            zone_pk: route.params.zone_pk,
            zone_slug: route.params.zone_slug,
            territory_pk: route.params.territory_pk,
            territory_slug: route.params.territory_slug,
            chapter_pk: route.params.chapter_pk,
            chapter_slug: route.params.chapter_slug
        },
        query: {
            page: $event
        }
    }
    if (chapter.value?.sector) {
        routeobj.name = "WorldForumSectorChapter"
        routeobj.params["sector_pk"] = route.params.sector_pk
        routeobj.params["sector_slug"] = route.params.sector_slug
    }
    router.push(routeobj)
}

const showWritingReply = ref(false)

const openNewReply = () => {
    showWritingReply.value = true
    setTimeout(() => {
        const el = document.getElementById("reply")
        el?.scrollIntoView()
    }, 100)
}

const closeNewReply = () => {
    showWritingReply.value = false
}

</script>
