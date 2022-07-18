<template>
    <div id="qp-app-header">
        <el-row :gutter="20" align="middle">
            <el-col :span="11" :lg="8">
                <div id="qp-header-logo">
                    <div id="qp-header-logo-img">
                        <el-image :src="logo" fit="cover">
                            <template #error>
                                <div class="image-slot"></div>
                            </template>
                        </el-image>
                    </div>
                    <div id="qp-header-logo-title">
                        <span v-text="'Cynorrs'"></span>
                    </div>
                </div>
                <div v-if="app.win.w >= 1200" id="qp-header-toggle-sidebar" @click="toggleSidebar()">
                    <el-icon class="mdi mdi-menu" />
                </div>
            </el-col>
            <el-col :span="2" :lg="8" class="text-center">
                <div id="qp-header-titlse">
                    <span v-text="'Cynorrs'"></span>
                </div>
            </el-col>
            <el-col :span="11" :lg="8">
                <div id="qp-header-menu">
                    <span v-text="'Cynorrs'"></span>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script setup>

import { computed, ref } from "vue";
import { useStore } from "vuex";

// =================================================================================== //

const store = useStore()
const app = computed(() => store.getters.app)

// =================================================================================== //
// ===--- DATA

const logo = ref(require("@/assets/img/logo-square-trans.png"))

const toggleSidebar = () => {
    store.commit("TOGGLE_SIDEBAR")
}

</script>

<style scoped>
    #qp-app-header {
        background-color: var(--qp-primary);
        box-shadow: 0 0 3px rgba(0, 0, 0, 0.04);
        box-sizing: border-box;
        height: 64px;
        position: relative;
        z-index: 1;
    }
    #qp-header-logo {
        display: inline-block;
        transition: opacity 0.4s;
        padding: 0 32px 0 0;
        margin: 0px 75px 0px 8px;
    }
    #qp-header-logo:hover {
        cursor: pointer;
        opacity: 0.6;
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
        color: var(--qp-bg);
        font-family: "Indie Flower", sans-serif;
        font-size: 32px;
        line-height: 120%;
        vertical-align: middle;
        display: inline-block;
    }
    #qp-header-toggle-sidebar {
        color: var(--qp-bg);
        font-size: 32px;
        line-height: 120%;
        vertical-align: middle;
        display: inline-block;
    }
    @media (max-width: 768px) {
        #qp-header-logo-title {
            display: none;
        }
    }
</style>
