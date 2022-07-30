<template>
    <div class="qp-vue">

        <div v-if="!isLoading && !hasError && world">
            <header class="qp-world-header">
                <h1 v-if="world.style && world.style.header == 'simple'" class="qp-world-header-name" @click="goToWorld()">
                    <span v-text="world.name"></span>
                </h1>
                <div v-else class="qp-container">
                    <el-row>
                        <el-col>
                            <qpCard pa="0">
                                <div class="qp-world-header-banner">
                                    <div class="qp-world-header-banner-inner">
                                        <el-image v-if="world.banner" :src="world.banner" fit="cover">
                                            <template #error>
                                                <div class="image-slot"></div>
                                            </template>
                                        </el-image>
                                    </div>
                                </div>
                                <div class="qp-world-header-identity">
                                    <h1 class="qp-world-header-identity-name" @click="goToWorld()">
                                        <span v-text="world.name"></span>
                                    </h1>
                                    <p class="qp-world-header-identity-description">
                                        <span v-text="world.description"></span>
                                    </p>
                                </div>
                            </qpCard>
                        </el-col>
                    </el-row>
                </div>
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

import qpCard from "@/components/basic/qpCard.vue";
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

<style scoped>
/* =- header */
.qp-world-header-banner {
    text-align: center;
    min-height: 250px;
    position: relative;
    margin: 0;
}
.qp-world-header-banner-inner  {
    background-color: var(--qp-default-disabled-bg);
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    overflow: hidden;
    height: 250px;
    margin: 0;
}
.qp-world-header-banner-inner .el-image {
    width: 100%;
    height: 100%;
    opacity: 0.9;
}
@media (max-width: 767px) {
    .qp-world-header-banner {
        min-height: 150px;
    }
    .qp-world-header-banner-inner  {
        height: 150px;
    }
}
/* ===--- identity ---=== */
.qp-world-header-identity {
    padding: 20px 12px 20px;
}
.qp-world-header-identity-name {
    font-family: "Quicksand", sans-serif;
    font-size: 64px;
    font-weight: 400;
    line-height: 120%;
    word-break: break-word;
    padding: 0;
    margin: 0 0 12px;
}
.qp-world-header-identity-description {
    font-family: "Roboto Condensed", sans-serif;
    font-size: 14px;
    font-weight: 400;
    font-style: italic;
    line-height: 120%;
    letter-spacing: 1px;
    opacity: 0.6;
    padding: 0;
    margin: 0 0 12px;
}
@media (max-width: 767px) {
    .qp-world-header-identity-name {
        font-size: 48px;
    }
}
</style>
