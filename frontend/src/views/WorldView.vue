<template>
    <div class="qp-vue">

        <div v-if="!isLoading && !hasError && world">
            <header class="qp-world-header">
                <h1 class="qp-world-header-name" @click="goToWorld()">
                    <span v-text="world.name"></span>
                </h1>
            </header>
            <router-view :key="$route.params.slug" :world="world" />
            <footer class="qp-world-footer">
                <div class="qp-world-footer-inner">
                    <el-row>
                        <el-col>
                            <div class="qp-world-footer-copyright">
                                <small>
                                    <span v-text="`&copy;&nbsp;${world.copyright} - ${$t('AllRightsReserved')}`"></span>
                                </small>
                            </div>
                        </el-col>
                    </el-row>
                </div>
            </footer>
        </div>

        <qpForumLoadError v-else :isloading="isLoading" :hasError="hasError" />

    </div>
</template>

<script setup>

import { computed, onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
import { API, SITE } from "@/main.js";
import i18n from "@/plugins/i18n";

import qpForumLoadError from "@/components/forum/core/qpLoadError.vue";

const { t } = i18n.global

const route = useRoute()
const router = useRouter()
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
            initMetadata(r.name)
            initStyle(r.style)
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

const initMetadata = (pagetitle) => {
     document.title = `${pagetitle} - ${SITE.name}`
}

const initStyle = (style) => {
    if (style) {
        let styletag;
        if (document.getElementById("qp-custom-style")) {
            styletag = document.getElementById("qp-custom-style")
        } else {
            styletag = document.createElement("style");
            styletag.setAttribute("id", "qp-custom-style");
        }
        styletag.innerHTML = `html,body{background-color:${style.app_body_bg};color:${style.app_body_txt};}`
        styletag.innerHTML += `#qp-app-header{--el-menu-text-color:${style.app_header_txt};--el-menu-active-color:${style.app_header_txt};--el-menu-hover-text-color:${style.app_header_txt_hov};background-color:${style.app_header_bg};}#app #qp-header-logo-title{color:${style.app_header_txt};}#app #qp-header-toggle-sidebar{color:${style.app_header_txt};}`
        styletag.innerHTML += `#qp-app-sidebar{background-color:${style.app_sidebar_bg};}#app #qp-sidebar-avatar{border-color:${style.app_sidebar_bg};}`
        styletag.innerHTML += `#qp-app-smallbar{background-color:${style.app_smallbar_bg};}`
        styletag.innerHTML += style.stylesheet;
        document.head.appendChild(styletag);
    }
}

const goToWorld = () => {
    if (route.name == "WorldForum") {
        router.go(route.fullPath)
    } else {
        router.push({name: "WorldForum", params: {slug: world.value.slug}})
    }
}

</script>
