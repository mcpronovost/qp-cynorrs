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

import { computed, onMounted, onBeforeUnmount, ref } from "vue";
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

onBeforeUnmount (() => {
    clearStyle()
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
    let styletag;
    if (document.getElementById("qp-custom-style")) {
        styletag = document.getElementById("qp-custom-style")
    } else {
        styletag = document.createElement("style");
        styletag.setAttribute("id", "qp-custom-style");
    }
    if (style) {
        styletag.innerHTML = `:root{`
        styletag.innerHTML += `--qp-primary:${style.primary};`

        styletag.innerHTML += `--qp-app-bg:${style.app_body_bg};`
        styletag.innerHTML += `--qp-app-txt:${style.app_body_txt};`

        styletag.innerHTML += `--qp-app-header-bg:${style.app_header_bg};`
        styletag.innerHTML += `--qp-app-header-txt:${style.app_header_txt};`
        styletag.innerHTML += `--qp-app-header-txt-hov:${style.app_header_txt_hov};`

        styletag.innerHTML += `--qp-app-sidebar-bg:${style.app_sidebar_bg};`
        styletag.innerHTML += `--qp-app-sidebar-txt:${style.app_sidebar_txt};`
        styletag.innerHTML += `--qp-app-sidebar-accent:${style.app_sidebar_accent};`

        styletag.innerHTML += `--qp-app-smallbar-bg:${style.app_smallbar_bg};`
        styletag.innerHTML += `--qp-app-smallbar-txt:${style.app_smallbar_txt};`
        styletag.innerHTML += `--qp-app-smallbar-accent:${style.app_smallbar_accent};`

        styletag.innerHTML += `--qp-default-bg:${style.default_bg};`
        styletag.innerHTML += `--qp-default-txt:${style.default_txt};`
        styletag.innerHTML += `--qp-default-accented-bg:${style.default_accented_bg};`
        styletag.innerHTML += `--qp-default-accented-txt:${style.default_accented_txt};`
        styletag.innerHTML += `--qp-default-disabled-bg:${style.default_disabled_bg};`
        styletag.innerHTML += `--qp-default-disabled-txt:${style.default_disabled_txt};`

        styletag.innerHTML += `--qp-form-bg:${style.form_bg};`
        styletag.innerHTML += `--qp-form-txt:${style.form_txt};`
        styletag.innerHTML += `--qp-form-placeholder:${style.form_placeholder};`
        styletag.innerHTML += `}`
        styletag.innerHTML += `${style.stylesheet}`
    } else {
        styletag.innerHTML = ""
    }
    document.head.appendChild(styletag);
}

const clearStyle = () => {

}

const goToWorld = () => {
    if (route.name == "WorldForum") {
        router.go(route.fullPath)
    } else {
        router.push({name: "WorldForum", params: {slug: world.value.slug}})
    }
}

</script>
