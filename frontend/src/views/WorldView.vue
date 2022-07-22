<template>
    <div class="qp-vue">

        <div v-if="!isLoading && !hasError && world">
            <header class="qp-world-header">
                <h1 class="qp-world-header-name">
                    <span v-text="world.name"></span>
                </h1>
            </header>
            <router-view :world="world" />
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

import qpForumLoadError from "@/components/forum/core/qpLoadError.vue";

const { t } = i18n.global

const route = useRoute()
const store = useStore()
const rat = computed(() => store.getters.rat)

const isLoading = ref(true)
const hasError = ref(null)

onMounted(() => {
    initWorld()
})

const world = ref(null)

const initWorld = async () => {
    isLoading.value = true
    hasError.value = null
    // ===---
    try {
        let response = await fetch(`${API}/worlds/${route.params.slug}/`, {
            method: "GET",
            headers: {"Authorization": rat.value}
        })
        let r = await response.json()
        if (response.status === 200) {
            world.value = r
        } else {
            throw response
        }
    } catch (e) {
        if (e.status === 403) {
            hasError.value = t("YouDoesntHaveAccessToThisWorld")
        } else if (e.status === 404) {
            hasError.value = t("ThisWorldDoesntExistAnymore")
        } else {
            hasError.value = t("AnErrorOccurred")
        }
    }
    // ===---
    isLoading.value = false
}

</script>
