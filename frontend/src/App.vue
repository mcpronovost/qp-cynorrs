<template>
    <div id="qp-app">
        <qpHeader />
        <qpSidebar />
        <div id="qp-app-main" :class="rat ? '' : 'qp-nosmallbar'">
            <el-scrollbar height="100%">
                <router-view :key="$route.fullPath" />
            </el-scrollbar>
        </div>
        <qpSmallbar />
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