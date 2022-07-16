<template>
    <div class="qp-vue">

        <div v-if="!isLoading && world" :class="`qp-forum qp-singleton-${singleton}`">
            <header class="qp-world-header">
                <h1 class="qp-world-header-name" @click="goToIndex()">
                    <span v-text="world.name"></span>
                </h1>
            </header>
            <div class="qp-container">
                <section v-if="route.name == 'World'" class="qp-forum-zones">
                    <qpForumZone v-for="(z, n) in world.zones" :key="`zones-${n}`" :world="world" :zone="z" :singleton="singleton" />
                </section>
                <section v-else-if="route.name == 'WorldZone'" class="qp-forum-zones">
                    <qpForumZone :world="world" :zone="zone" :singleton="singleton" />
                </section>
                <section v-else-if="route.name == 'WorldTerritory'" class="qp-forum-territories">
                    <qpForumTerritory :world="world" :zone="zone" :territory="territory" :singleton="singleton" />
                </section>
                <section v-else-if="route.name == 'WorldSector'" class="qp-forum-sectors">
                    <qpForumSector :world="world" :zone="zone" :territory="territory" :sector="sector" :singleton="singleton" />
                </section>
                <section v-else-if="route.name == 'WorldChapter'" class="qp-forum-chapters">
                    <qpForumChapter :world="world" :zone="zone" :territory="territory" :sector="sector" :chapter="chapter" :singleton="singleton" />
                </section>
            </div>
            <footer class="qp-world-footer">
                <small>&copy;&nbsp;<span v-text="world.copyright.year"></span></small>
            </footer>
        </div>

        <div v-else-if="isLoading">
            <div class="qp-container">
                <div v-loading="isLoading" element-loading-background="transparent" style="height:200px"></div>
            </div>
        </div>

        <div v-else-if="hasError">
            <div class="qp-container">
                <el-result icon="error" :title="t('Error')" :sub-title="hasError" />
            </div>
        </div>
    </div>
</template>

<script setup>

import { computed, onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
import { API } from "@/main.js";
import i18n from "@/plugins/i18n";

import qpForumZone from "@/components/forum/qpZone.vue";
import qpForumTerritory from "@/components/forum/qpTerritory.vue";
import qpForumSector from "@/components/forum/qpSector.vue";
import qpForumChapter from "@/components/forum/qpChapter.vue";

const { t } = i18n.global

// =================================================================================== //

const route = useRoute()
const router = useRouter()

const store = useStore()
const rat = computed(() => store.getters.rat)

const isLoading = ref(true)
const hasError = ref()
const world = ref()
const zone = ref()
const territory = ref()
const sector = ref()
const chapter = ref()
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
    let q = ""
    if ("page" in route.query && Number(route.query.page) > 0) {
        q = `?page=${Number(route.query.page)}`
    }
    // ===---
    let r = await fetch(`${API}/worlds/territories/${territoryPk}/${q}`, {
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

const setSector = async (sectorPk) => {
    isLoading.value = true
    hasError.value = null
    let q = ""
    if ("page" in route.query && Number(route.query.page) > 0) {
        q = `?page=${Number(route.query.page)}`
    }
    // ===---
    let r = await fetch(`${API}/worlds/sectors/${sectorPk}/${q}`, {
        method: "GET",
        headers: {"Authorization": rat}
    })
    if (r.status === 200) {
        let result = await r.json()
        world.value = result.world
        zone.value = result.zone
        territory.value = result.territory
        sector.value = result.sector
        initStyle(result.world.stylesheet)
    } else {
        hasError.value = t("ThisSectorDoesntExistAnymore")
    }
    isLoading.value = false
    // ===---
}

const setChapter = async (chapterPk) => {
    isLoading.value = true
    hasError.value = null
    let q = ""
    if ("page" in route.query && Number(route.query.page) > 0) {
        q = `?page=${Number(route.query.page)}`
    }
    // ===---
    let r = await fetch(`${API}/worlds/chapters/${chapterPk}/${q}`, {
        method: "GET",
        headers: {"Authorization": rat}
    })
    if (r.status === 200) {
        let result = await r.json()
        world.value = result.world
        zone.value = result.zone
        territory.value = result.territory
        sector.value = result.sector
        chapter.value = result.chapter
        initStyle(result.world.stylesheet)
    } else {
        hasError.value = t("ThisChapterDoesntExistAnymore")
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

const goToIndex = () => {
    if (route.name == "World") {
        router.go()
    } else {
        router.push({name: "World", params: {
            world_pk: world.value.id,
            slug: world.value.slug
        }})
    }
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
    } else if (route.name == 'WorldSector') {
        singleton.value = "sector"
        setSector(route.params.sector_pk)
    } else if (route.name == ('WorldChapter'||'WorldSectorChapter')) {
        singleton.value = "chapter"
        setChapter(route.params.chapter_pk)
    }
})

// =================================================================================== //

</script>
