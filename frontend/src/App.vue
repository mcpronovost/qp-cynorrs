<template>
    <div id="qp-app">
        <qp-header />
        <qp-sidebar />
        <div id="qp-app-main">
            <el-scrollbar height="100%">
                <router-view />
            </el-scrollbar>
        </div>
        <qp-smallbar />
    </div>
</template>

<script>
import qpHeader from "@/components/core/qpHeader.vue";
import qpSidebar from "@/components/core/qpSidebar.vue";
import qpSmallbar from "@/components/core/qpSmallbar.vue";
export default {
    name: "App",
    components: {
        qpHeader,
        qpSidebar,
        qpSmallbar
    },
    data () {
        return {
            test: this.$route
        }
    }
};
</script>
