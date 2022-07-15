<template>
    <div id="qp-app">
        <qpHeader />
        <qpSidebar />
        <div id="qp-app-main">
            <el-scrollbar height="100%">
                <router-view :key="$route.path" />
            </el-scrollbar>
        </div>
        <qpSmallbar />
    </div>
</template>

<script setup>
import qpHeader from "@/components/core/qpHeader.vue";
import qpSidebar from "@/components/core/qpSidebar.vue";
import qpSmallbar from "@/components/core/qpSmallbar.vue";
</script>

<style>
    @import url("./assets/css/cynorrs.css");
</style>