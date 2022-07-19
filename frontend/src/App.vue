<template>
    <div id="qp-app">
        <qpHeader v-if="!$route.name || !$route.name.startsWith('Auth')" />
        <qpSidebar v-if="!$route.name || !$route.name.startsWith('Auth')" />
        <div id="qp-app-main" :class="`${(rat ? '' : ' qp-nosmallbar')}${($route.name && $route.name.startsWith('Auth') ? ' qp-fullview' : '')}`">
            <el-scrollbar height="100%">
                <router-view :key="$route.fullPath" />
            </el-scrollbar>
        </div>
        <qpSmallbar v-if="!$route.name || !$route.name.startsWith('Auth')" />
    </div>
</template>

<script setup>

import { computed } from "vue";
import { useStore } from "vuex";

import qpHeader from "@/components/core/qpHeader.vue";
import qpSidebar from "@/components/core/qpSidebar.vue";
import qpSmallbar from "@/components/core/qpSmallbar.vue";

// =================================================================================== //

const store = useStore()
const rat = computed(() => store.getters.rat)

</script>

<style>
    @import url("./assets/css/cynorrs.css");
</style>