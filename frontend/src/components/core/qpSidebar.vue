<template>
    <div id="qp-app-sidebar" :class="app.win.w < 1200 || app.sidebar?.collapse ? 'qp-collapsed' : ''">
        <el-scrollbar height="100%">
            <div id="qp-sibebar-inner">
                <div id="qp-sibebar-main">
                    <qpSidebarProfile />
                    <qpSidebarNav />
                </div>
                <div id="qp-sidebar-footer">
                    <span v-html="$t('TextCopyrights')"></span>
                </div>
            </div>
        </el-scrollbar>
    </div>
</template>

<script setup>

import { computed } from "vue";
import { useStore } from "vuex";

import qpSidebarProfile from "@/components/core/qpSidebarProfile.vue";
import qpSidebarNav from "@/components/core/qpSidebarNav.vue";

// =================================================================================== //

const store = useStore()
const app = computed(() => store.getters.app)

</script>

<style scoped>
    #qp-sibebar-inner {
        display: flex;
        flex-direction: column;
        height: calc(100vh - 64px);
    }
    #qp-sibebar-main {
        flex: 1 1 auto;
    }
    #qp-sidebar-footer {
        color: var(--qp-secondary);
        font-size: 12px;
        line-height: 120%;
        text-align: center;
        flex: 0 0 auto;
        padding: 12px;
    }
    @media (max-width: 1199px) {
        #qp-app-sidebar {
            width: 10vw;
            min-width: 64px;
        }
    }
</style>
