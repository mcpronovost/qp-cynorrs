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

        <div v-else-if="isLoading">
            <div class="qp-container">
                <div v-loading="isLoading" element-loading-background="transparent" style="height:60vh"></div>
            </div>
        </div>

        <div v-else>
            <div class="qp-container">
                <qpCard h="auto">
                    <el-result icon="error" :title="$t('Error')" :sub-title="hasError" />
                </qpCard>
            </div>
        </div>

    </div>
</template>

<script setup>

import { computed, onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import { useStore } from "vuex";
import { API } from "@/main.js";
import i18n from "@/plugins/i18n";

import qpCard from "@/components/basic/qpCard.vue";

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
        if (e.status === 404) {
            hasError.value = t("ThisWorldDoesntExistAnymore")
        } else {
            hasError.value = t("AnErrorOccurred")
        }
    }
    // ===---
    console.log("what")
    isLoading.value = false
}

</script>
