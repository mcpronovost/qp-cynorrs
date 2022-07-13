<template>
    <div class="qp-vue">
        <div class="qp-container">

            <div v-if="!isLoading && world" :class="`qp-forum qp-singleton-${singleton}`">
                <section class="qp-forum-zones">
                    <qpForumZone v-for="(zone, n) in world.zones" :key="`zones-${n}`" :zone="zone" :singleton="singleton" />
                </section>
            </div>

            <div v-else-if="isLoading">
                <div v-loading="isLoading" element-loading-background="transparent" style="height:200px"></div>
            </div>

            <div v-else-if="hasError">
                <el-result icon="error" :title="t('Error')" :sub-title="hasError" />
            </div>

        </div>
    </div>
</template>

<script setup>

import { computed, onBeforeUnmount, onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import { useStore } from "vuex";
import { API } from "@/main.js";
import i18n from "@/plugins/i18n";

import qpForumZone from "@/components/forum/qpZone.vue";

const { t } = i18n.global

// =================================================================================== //

const route = useRoute()

const store = useStore()
const rat = computed(() => store.getters.rat)

const isLoading = ref(true)
const hasError = ref()
const world = ref()
const singleton = ref("index")

// =================================================================================== //
// ===--- METHODS

const setWorld = async (worldPk) => {
    isLoading.value = true
    hasError.value = null
    // ===---
    let r = await fetch(`${API}/worlds/${worldPk}/`, {
        method: "GET",
        headers: {"Authorization": rat}
    })
    if (r.status === 200) {
        let result = await r.json()
        world.value = result.world
        initStyle(result.world.stylesheet)
    } else {
        hasError.value = t("ThisWorldDoesntExistAnymore")
    }
    isLoading.value = false
    // ===---
}

const initStyle = (stylesheet) => {
    let styletag = document.createElement("style");
    styletag.setAttribute("id", "qp-custom-style");
    styletag.innerHTML = stylesheet;
    document.head.appendChild(styletag);
}

// =================================================================================== //

onMounted(() => {
    setWorld(route.params.world_pk)
})

onBeforeUnmount(() => {
    document.getElementById("qp-custom-style").remove();
})

// =================================================================================== //

</script>
