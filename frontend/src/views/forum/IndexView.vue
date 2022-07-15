<template>
    <div class="qp-vue">
        <div class="qp-container">

            <div v-if="!isLoading && world" :class="`qp-forum qp-singleton-${singleton}`">
                <section v-if="route.name == 'World'" class="qp-forum-zones">
                    <qpForumZone v-for="(z, n) in world.zones" :key="`zones-${n}`" :world="world" :zone="z" :singleton="singleton" />
                </section>
                <section v-else-if="route.name == 'WorldZone'" class="qp-forum-zones">
                    <qpForumZone :world="world" :zone="zone" :singleton="singleton" />
                </section>
                <section v-else-if="route.name == 'WorldTerritory'" class="qp-forum-territories">
                    <qpForumTerritory :world="world" :zone="zone" :territory="territory" :singleton="singleton" />
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

import { computed, onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import { useStore } from "vuex";
import { API } from "@/main.js";
import i18n from "@/plugins/i18n";

import qpForumZone from "@/components/forum/qpZone.vue";
import qpForumTerritory from "@/components/forum/qpTerritory.vue";

const { t } = i18n.global

// =================================================================================== //

const route = useRoute()

const store = useStore()
const rat = computed(() => store.getters.rat)

const isLoading = ref(true)
const hasError = ref()
const world = ref()
const zone = ref()
const territory = ref()
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

const setZone = async (zonePk) => {
    isLoading.value = true
    hasError.value = null
    // ===---
    let r = await fetch(`${API}/worlds/zones/${zonePk}/`, {
        method: "GET",
        headers: {"Authorization": rat}
    })
    if (r.status === 200) {
        let result = await r.json()
        world.value = result.world
        zone.value = result.zone
        initStyle(result.world.stylesheet)
    } else {
        hasError.value = t("ThisZoneDoesntExistAnymore")
    }
    isLoading.value = false
    // ===---
}

const setTerritory = async (territoryPk) => {
    isLoading.value = true
    hasError.value = null
    // ===---
    let r = await fetch(`${API}/worlds/territories/${territoryPk}/`, {
        method: "GET",
        headers: {"Authorization": rat}
    })
    if (r.status === 200) {
        let result = await r.json()
        world.value = result.world
        zone.value = result.zone
        territory.value = result.territory
        initStyle(result.world.stylesheet)
    } else {
        hasError.value = t("ThisTerritoryDoesntExistAnymore")
    }
    isLoading.value = false
    // ===---
}

const initStyle = (stylesheet) => {
    let styletag;
    if (document.getElementById("qp-custom-style")) {
        styletag = document.getElementById("qp-custom-style")
    } else {
        styletag = document.createElement("style");
        styletag.setAttribute("id", "qp-custom-style");
    }
    styletag.innerHTML = stylesheet;
    document.head.appendChild(styletag);
}

// =================================================================================== //

onMounted(() => {
    if (route.name == 'World') {
        singleton.value = "index"
        setWorld(route.params.world_pk)
    } else if (route.name == 'WorldZone') {
        singleton.value = "zone"
        setZone(route.params.zone_pk)
    } else if (route.name == 'WorldTerritory') {
        singleton.value = "territory"
        setTerritory(route.params.territory_pk)
    }
})

// =================================================================================== //

</script>
