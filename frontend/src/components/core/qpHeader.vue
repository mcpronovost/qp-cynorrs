<template>
    <div id="qp-app-header">
        <el-row :gutter="20" align="middle">
            <el-col :span="10" class="text-left">
                <div id="qp-header-logo" @click="goToHome()">
                    <div id="qp-header-logo-img">
                        <el-image :src="logo" fit="cover">
                            <template #error>
                                <div class="image-slot"></div>
                            </template>
                        </el-image>
                    </div>
                    <div id="qp-header-logo-title">
                        <span v-text="SITE.shortname"></span>
                    </div>
                </div>
                <div v-if="app.win.w >= 1200" id="qp-header-toggle-sidebar" @click="toggleSidebar()">
                    <el-icon>
                        <Expand v-if="app.sidebar.collapse" />
                        <Fold v-else />
                    </el-icon>
                </div>
                <div id="qp-header-menu-app">
                    <el-menu router mode="horizontal" menu-trigger="click">
                        <el-menu-item disabled index="discover">
                            <span v-text="$t('Discover')"></span>
                        </el-menu-item>
                        <el-menu-item disabled index="browse">
                            <span v-text="$t('Browse')"></span>
                        </el-menu-item>
                    </el-menu>
                </div>
            </el-col>
            <el-col :span="14" class="text-right">
                <qpHeaderNavPlayer />
            </el-col>
        </el-row>
    </div>
</template>

<script setup>

import { computed, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
import { SITE } from "@/main.js";

import { Expand, Fold } from "@element-plus/icons-vue";
import qpHeaderNavPlayer from "@/components/core/qpHeaderNavPlayer.vue";

const route = useRoute()
const router = useRouter()
const store = useStore()
const app = computed(() => store.getters.app)

const logo = ref(require("@/assets/img/logo-square-trans.png"))

const goToHome = () => {
    if (route.name == "Home") {
        router.go(route.fullPath)
    } else {
        router.push({name: "Home"})
    }
}

const toggleSidebar = () => {
    store.commit("TOGGLE_SIDEBAR")
}

</script>

<style scoped>
    /* ===--- logo ---=== */
    #qp-header-logo {
        color: var(--qp-app-header-txt);
        display: inline-block;
        transition: color 0.4s;
        padding: 0 32px 0 0;
        margin: 0px 75px 0px 0;
    }
    #qp-header-logo:hover {
        color: var(--qp-app-header-txt-hov);
        cursor: pointer;
    }
    #qp-header-logo-img {
        background-color: #505f65;
        border-radius: 100%;
        overflow: hidden;
        vertical-align: middle;
        display: inline-block;
        width: 42px;
        height: 42px;
        margin: 0 12px;
    }
    #qp-header-logo-img .el-image {
        width: 100%;
        height: 100%;
    }
    #qp-header-logo-title {
        font-family: "Indie Flower", sans-serif;
        font-size: 32px;
        line-height: 120%;
        vertical-align: middle;
        display: inline-block;
    }
    @media (max-width: 1199px) {
        #qp-header-logo {
            padding: 0;
            margin: 0;
        }
    }
    @media (max-width: 767px) {
        #qp-header-logo {
            padding: 0;
            margin: 0;
        }
        #qp-header-logo-title {
            display: none;
        }
    }
    /* ===--- toggle-sidebar ---=== */
    #qp-header-toggle-sidebar {
        color: var(--qp-app-header-txt);
        font-size: 24px;
        line-height: 0;
        vertical-align: middle;
        display: inline-block;
        transition: color 0.4s;
    }
    #qp-header-toggle-sidebar:hover {
        color: var(--qp-app-header-txt-hov);
        cursor: pointer;
    }
    /* ===--- MENU-APP ---=== */
    #qp-header-menu-app {
        vertical-align: middle;
        display: inline-block;
        width: calc(100% - 350px);
        margin: 0 0 0 32px;
    }
    @media (max-width: 1199px) {
        #qp-header-menu-app {
            width: calc(100% - 230px);
        }
    }
    @media (max-width: 767px) {
        #qp-header-menu-app {
            width: calc(100% - 90px);
            margin: 0;
        }
    }
</style>
